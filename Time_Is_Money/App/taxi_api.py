#Essentials
import numpy as np
import pandas as pd
import pickle
import datetime as dt

#Regression imports
from sklearn.preprocessing import StandardScaler

import geopy.distance as gd
from shapely.geometry import Point

#Geography magic
import geocoder
import gmplot

#SQL related
import psycopg2
# from time_is_money import time_is_money

# import time_is_money as tim
import geocoder

test_ride = {'origin': '401 N Wabash Ave, Chicago', 'destination': '1033 West Van Buren Street, Chicago',
             'now': 'No', 'year': 2017, 'month': 4, 'day': 27, 'hour': 5, 'minute': 0, 'ampm': 'AM'}

def get_latitude(address):
    """Takes an address string and converts it into a lat/long.
    Returns longitude and longitude pair."""
    latitude = geocoder.osm(address).latlng[0]
    return latitude

def get_longitude(address):
    """Takes an address string and converts it into a lat/long.
    Returns longitude and longitude pair."""
    longitude = geocoder.osm(address).latlng[1]
    return longitude

def get_coordinates(origin, destination):
    """Takes origin and destination addresses and returns two lists, one with latitudes, second with longitudes"""
    latitudes = [get_latitude(origin), get_latitude(destination)]
    longitudes = [get_longitude(origin), get_longitude(destination)]

    result = {'latitudes': latitudes,
                'longitudes': longitudes}
    return result

def get_distance(origin_address, destination_address):
    """Takes origin and destination addresses, converts them into geopoints and returns distance (in miles).
    Returns distance float (in miles)."""
    origin = (get_latitude(origin_address), get_longitude(origin_address))
    destination = (get_latitude(destination_address), get_longitude(destination_address))
    distance = gd.geodesic(origin, destination).miles
    return distance

def get_now():
    """Returns current timestamp."""
    now = dt.datetime.now()
    return now

def get_demand(datetime_start, datetime_end):
    """Uses a date and time object as input.
    Returns a dataframe with historic demand given the datetime"""

    # Set up the database connection
    conn = psycopg2.connect(dbname="taxi_rides_db", user="auste_m")
    query_demand = f"""SELECT trip_start_timestamp, COUNT(trip_start_timestamp) as interval_demand
                        FROM taxi_rides
                        WHERE trip_start_timestamp BETWEEN '{datetime_start}' AND '{datetime_end}'
                        GROUP BY trip_start_timestamp
                        ORDER BY trip_start_timestamp"""
    demand_last_week = pd.read_sql_query(query_demand, conn)
    demand_last_week = demand_last_week.set_index(['trip_start_timestamp'])
    return demand_last_week

def get_hist_demand(demand_df):
    """Takes a demand dataframe with timestamp as index and interval demand column.
    Returns a differenced dataframe with 9 columns with NaN values dropped."""
    diffed_demand = demand_df.diff()
    diffed_demand = diffed_demand[1:]

    #Create lags
    diffed_demand['demand_lag1'] = diffed_demand['interval_demand'].shift(1)
    diffed_demand['demand_lag2'] = diffed_demand['interval_demand'].shift(2)
    diffed_demand['demand_lag3'] = diffed_demand['interval_demand'].shift(3)
    diffed_demand['demand_lag4'] = diffed_demand['interval_demand'].shift(4)
    diffed_demand['demand_lag5'] = diffed_demand['interval_demand'].shift(5)
    diffed_demand['demand_lag6'] = diffed_demand['interval_demand'].shift(6)
    diffed_demand['demand_lag7'] = diffed_demand['interval_demand'].shift(7)
    diffed_demand['demand_lag96'] = diffed_demand['interval_demand'].shift(96)
    diffed_demand['demand_lag672'] = diffed_demand['interval_demand'].shift(672)

    #Drop rows with NaN values
    diffed_demand = diffed_demand.dropna()

    #Drop the interval_demand column
    diffed_demand = diffed_demand.drop(columns=['interval_demand'])
    return diffed_demand

def get_weather(desired_datetime):
    """Takes a date and time object and retrieves the weather conditions for that day.
    Returns a dataframe with weather conditions."""
    # Set up the database connection
    conn = psycopg2.connect(dbname="taxi_rides_db", user="auste_m")

    query_weather = f"""SELECT avg_daily_wind_speed, avg_temp_f, fog, rain, snow
                         FROM chicago_weather
                         WHERE date = CAST('{desired_datetime}' AS DATE)"""
    weather_today = pd.read_sql_query(query_weather, conn)
    weather_today = weather_today.fillna(value=0)
    return weather_today


def get_scaled_features(feature_space):
    """Takes feature space and scales it onto the scale of 0 to 1
    in order to avoid inflating certain variables simply due to their inherently higher numeric values.
    Returns a scaled feature space."""
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(feature_space)
    return scaled_features

def get_ETA(trip_duration, start_time=dt.datetime.now()):
    """Takes current datetime and trip duration as input.
    Returns Estimated Time of Arrival."""
    now = start_time
    ETA = now + dt.timedelta(seconds=trip_duration)
    ETA = ETA.strftime("%Y-%m-%d %I:%M%p")
    return ETA

def plot_route(origin, destination):
    """Takes origin and destination coordinates and generates a route on Chicago City map.
    Generates a plot with origin and destination marked and a straight line between the two points."""
    latitudes = [get_latitude(origin), get_latitude(destination)]
    longitudes = [get_longitude(origin), get_longitude(destination)]

    taxi_route = gmplot.GoogleMapPlotter.from_geocode('Chicago, USA')

    #Plot the dots
    taxi_route.scatter(latitudes, longitudes, 'magenta', size=200, marker=False)

    #Plot the line
#     taxi_route.plot(latitudes, longitudes, 'blue', edge_width = 2.5)

    # Draw
    taxi_route.draw("./Chicago_taxi_route.html")

def time_is_money(origin, destination, now, year=0, month=0, day=0, hours=0, minutes=0, ampm='AM'):
    """This functions takes origin and destination addresses (in Chicago) and a date and time.
    Returns an ETA prediction and fare estimate."""
    #Get or just format the datetime
    if now == 'yes':
        desired_time = get_now()
    elif ampm == 'AM':
        desired_time = dt.datetime(year, month, day, hours, minutes)
    else:
        desired_time = dt.datetime(year, month, day, hours + 12, minutes)

    time_week_ago = desired_time - dt.timedelta(days=7, minutes=15)

    #GET LAT/LONGS FOR FOR ORIGIN AND DESTINATION ADDRESSES
    origin_lat = get_latitude(origin)
    origin_long = get_longitude(origin)
    destination_lat = get_latitude(destination)
    destination_long = get_longitude(destination)

    #Get weather conditions
    weather_today = get_weather(desired_time)

    #Get the demand for the last 1h 45min, same time yesterday and same time 7 days ago
    demand_last_week_diffed = get_hist_demand(get_demand(time_week_ago, desired_time))

    #Pull in trained linear regression model to predict current demand
    with open('../LinearRegression_demand.pkl', 'rb') as pickle_demand:
        LinReg_demand = pickle.load(pickle_demand)

    #Predict demand growth / decline
    predicted_demand_diff = list(LinReg_demand.predict(demand_last_week_diffed))

    #Design feature space
    weekday = desired_time.weekday()
    trip_miles = get_distance(origin, destination)
    trip_log_miles = np.log(trip_miles)

    features = weather_today
    features['weekday'] = weekday
    features['predicted_demand_diff'] = predicted_demand_diff
    features['trip_log_miles'] = trip_log_miles
    features['origin_lat'] = origin_lat
    features['origin_long'] = origin_long
    features['destination_lat'] = destination_lat
    features['destination_long'] = destination_long

    #Scale features
    scaled_features = get_scaled_features(features)

    #Pull in trained Random Forest models to predict personalized ETA and fare based on the locations and time
    with open('../RandomForest_ETA_predictor.pkl', 'rb') as pickle_ETA:
        RandomForest_ETA_predictor = pickle.load(pickle_ETA)
    with open('../RandomForest_fare_predictor.pkl', 'rb') as pickle_fare:
        RandomForest_fare_predictor = pickle.load(pickle_fare)

    #Predict the log duration, exponentiate to get seconds and convert to an ETA
    seconds_log = RandomForest_ETA_predictor.predict(scaled_features)
    seconds = np.exp(seconds_log)
    ETA = get_ETA(int(seconds), desired_time)

    #Predict the log fare, exponentiate to get dollars
    fare_log = RandomForest_fare_predictor.predict(scaled_features)
    fare = round(np.exp(int(fare_log)), 2)

    return {'ETA': ETA, 'Fare': fare}

def make_prediction(features):
    feat_space = {'origin': features['origin'], 'destination': features['destination'], 'now': features['now'],
                            'year': features['year'], 'month': features['month'], 'day': features['day'],
                            'hours': features['hours'], 'minutes': features['minutes'], 'ampm': features['ampm']}

    both_predictions = time_is_money(**feat_space)   #**test_ride

    ETA = both_predictions['ETA']
    fare = both_predictions['Fare']

    result = {'ETA': ETA,
                'fare': fare}
    return result

if __name__ == '__main__':
    print(make_prediction(test_ride))
