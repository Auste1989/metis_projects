## Transit Time and Rate Calculator

### Problem:
How long will it take you to get to your destination and how much will it cost?

#### Description:
I will be analyzing Chicago City Taxi Ride dataset combined with weather data in order to predict Estimated Time of Arrival (ETA) and the cost of the ride (excluding tip). The ultimate goal of the MVP is to provide the user with an application that estimates an ETA and rate for a taxi ride based on origin and destination (addresses) and a current timestamp.

### Why?
Accurate pricing and potential delay detection due to weather are some of the most pressing issues in transportation industry. As a representative of this industry, I see a lot of potential for such application at my current employer.

### About The Dataset
I am using Chicago City **Taxi Ride** dataset. It's very large, I am using 2015, 2016 for training and 2017-01 to 2017-08 for testing, which is roughly 20GB. I have started off with working on my local machine, but might have to put it up on the cloud or work with pySpark (or both).

Some cleanup has already been done, but more EDA effort will certainly be needed.  
*I am not planning to use all of the data, but potentially take a subset of it, to begin with.*  
More information about the **taxi ride** dataset can be found [here](https://digital.cityofchicago.org/index.php/chicago-taxi-data-released/).

The **Weather dataset** contains daily precipitation, snowfall, snow depth, maximum / minimum temperatures and flag for weather tags (such as thunder, heavy fog, tornado, etc.).  
More information about **weather** dataset can found [here](https://www.ncdc.noaa.gov/).

Another small dataset will be needed for converting addresses to lat/longs.
Also I will need shape files for Chicago city map and roads to be able to plot and potentially map out the routes.

### Approach
The general plan is to get the data into postgreSQL database, clean & massage it, form one dataset (combined taxi ride and weather info) and train a multiple linear regression model to estimate an ETA and fare.
*Depending on the results, I'll have to try out other modelling techniques.*

#### Plan of Action
1. Get the data using City of Chicago API and NOAA service (for weather) :thumbsup:
  * Find the links between taxi ride dataset and weather dataset - *easy - date!* :thumbsup:
2. Store the information in a postgreSQL database (on local machine and AWS) *(ran out of memory on the cloud)* :thumbsup:
3. Do thorough analysis of the data :thumbsup:
4. Take appropriate cleaning steps (including dummification): :thumbsup:
    * Calculate base rate including tolls :thumbsup:
5. Do the train-test split (set aside test set) *no train-test split needed, set aside 2017 data* :thumbsup:
6. Difference the time series data :thumbsup:
7. Run Autocorrelation analysis to understand how many lags should be included as features :thumbsup:
8. Try moving average technique
9. Assess the results of time series OLS
10. Scale the data before modelling (to avoid inflation of the importance of certain features)
11. Run a GridSearch for the parameters for each of the following models:
    * Linear Regression :thumbsdown:
    * Ridge :thumbsdown:
    * Lasso :thumbsdown:
    * Random Forest :thumbsup:
    * XGBoost :thumbsdown:
12. Get Cross-Validation RMSE scores for each model :thumbsup:
13. Choose the best model :thumbsup:
13. Check the learning curve :thumbsup:
14. Test the model on the test set and assess the results
15. Write a few helper functions:
    * Convert an address to lat-longs :thumbsup:
    * Generate date and time of now :thumbsup:
    * Plot the route using GoogleMaps API :smirk: *plotted the points, but no route*
16. Summarize the findings
17. Build a Flask app *in progress*
18. Build the presentation :thumbsup:
19. Practice, practice, practice


### Progress Notes
2. I was able to create psql databases on AWS, but the moment I started trying to run any commands it gave me "Run Out of Memory" error. Therefore I decided to not waste much more time and do it on my local machine (I might have re-attempt doing it on AWS if my local machine starts failing).  
2. Initial dataset (full 2016 data was just short of 20 mln records). I created two tables in SQL, one for taxi rides and one for weather. When pulling it into jupyter notebook, I joined them on date creating one dataset.  
3. A lot of the records had missing location coordinates and quite some outliers where observed. Also, interestingly, rides paid for by credit card had a higher mean & median fare, due to longer distance or duration trips. This is likely attributable to trips taken by business men & women. This is merely an observation and doesn't play any role in my model.
3. Visual time series analysis showed that weekday and time of the day has an impact on fares and taxi demand.    
4. During cleaning, I dropped NaN and zero values from distance, duration, fare and location columns as well as removed records with extreme miles / hour, fare / mile and fare / minute. The final number of records after cleaning was just over 12 mln (or 62% of the original dataset).  
4. Tolls were added to the base fare right in the beginning when querying the data from PSQL, since in Chicago taxi ride fares do not include tolls.  
5. I worked on only 2016 data for training the model and used 2017 Jan-Aug dataset as test set  
6. Dickey-Fuller test indicated that my time series data wasn't stationary (SHOCKER! :astonished:). This suggests that differencing is needed to remove the trend / pattern. A quick test showed that differencing once is an optimal solution (standard deviation is at the minimum after differencing once).  
7. Partial Autocorrelation plot indicated that in order to capture historical demand effects I should take 7 first lags, 96th lag and 672nd lag (corresponding to last 1h 45min, same time yesterday and same time a week ago).  
8. Average moving technique is not needed, due to already implemented differencing and lagging techniques.  
9. Time series model with above mentioned lags produces RMSE score of 32.0 (less than 1 standard deviation). I would like to also try facebook's prophet *(installing it crashed my matplotlib), so I'll try again if there's time*.  
10. My feature space is as follows:
    * weekday (**float**)
    * predicted demand
    * trip_miles (float)
    * pickup_centroid_latitude (float)
    * pickup_centroid_longitude (float)
    * dropoff_centroid_latitude (float)
    * dropoff_centroid_longitude (float)
    * avg_temp_f (float)
    * fog (boolean)
    * rain (boolean)
    * snow (boolean)
First go is without scaling. I will try and scale all the features to avoid inflating the importance of variables that have higher numeric values.  
12. Here are the RMSE scores:
    * Linear Regression **44%**
    * Ridge **44%**
    * Lasso **44%**
    * Random Forest **36%**
    * XGBoost  **86%** *terrible!*
13. Going for Random Forest for both ETA and fare. It performed the best given the amount of time I had to play around with hyper-parameters
14. Learning curve was good, not a lot of discrepancy between training and testing scores. More data would likely make the model slightly better, so I might train the final model with 2 month's worth of data instead of 1.
17. Some fun facts:
  * Interestingly, when looking at feature importance, for ETA prediction demand seems to be the seconds most important feature after distance, whereas it is pretty insignificant when estimating the fare. This is clearly the result of lack of transparency in the regular taxi business (unlike Lyft / Uber).   
  * Out of all the features, weather related variables have close to no influence on the either duration or fare of a taxi trip.
  * 
