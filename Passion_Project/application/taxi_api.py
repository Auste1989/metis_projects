import numpy as np
import time_is_money as tim
import geocoder

test_ride = {'origin': '401 N Wabash Ave, Chicago', 'destination': '1033 West Van Buren Street, Chicago', 'when': 'yes'}

def make_prediction(features):
    feat_space = np.array([features['origin'], features['destination'], features['time'],
                            features['year'], features['month'], features['day'],
                            features['hours'], features['minutes']).reshape(1,-1)

    both_predictions = tim.time_is_money(feat_space)

    ETA = both_predictions['ETA']
    fare = both_predictions['Fare']

    result = {'ETA': ETA,
                'fare': fare}
    return result

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

    latitudes = [get_latitude(origin), get_latitude(destination)]
    longitudes = [get_longitude(origin), get_longitude(destination)]

    result = {'latitudes': latitudes,
                'longitudes': longitudes}
    return result

if __name__ == '__main__':
    print(make_prediction(test_ride))
