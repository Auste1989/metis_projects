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
2. Store the information in a postgreSQL database (on local machine and AWS) *(ran out of memory on the cloud)* :thumbsup:
3. Do thorough analysis of the data :thumbsup:
4. Take appropriate cleaning steps (including dummification): :thumbsup:
    * Calculate base rate including tolls :thumbsup:
5. Find the links between taxi ride dataset and weather dataset - *easy - date!* :thumbsup:
6. Do the train-test split (set aside test set) *no train-test split needed, set aside 2017 data* :thumbsup:
7. Difference the time series data
8. Run Autocorrelation analysis to understand how many lags should be included as features
9. Try moving average technique
7. Scale the data before modelling (to avoid inflation of the importance of certain features)
8. Run a CV search for the best model and parameters
9. Get Cross-Validation scores for the best model
10. Examine the learning curve and train the model with more data, if needed
11. Test the model on the test dataset and assess the results
12. Write a helper function that would allow to easily convert addresses (based on postal codes) to lat-longs
12. Summarize the findings
13. Build a Flask app
13. Build the presentation
14. Practice, practice, practice
