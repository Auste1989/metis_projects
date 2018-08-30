Drop-off## Transit Time and Rate Calculator

### Problem:
How long will it take you to get to your destination and how much will it cost?

#### Description:
I will be analyzing Chicago City Taxi Ride dataset combined with weather data in order to predict Estimated Time of Arrival (ETA) and the cost of the ride (excluding tip). The ultimate goal of the MVP is to provide the user with an application that estimates an ETA and rate for a taxi ride based on origin and destination (addresses) and a current timestamp.

### Why?
Accurate pricing and potential delay detection due to weather are some of the most pressing issues in transportation industry. As a representative of this industry, I see a lot of potential for such application at my current employer.

### About The Dataset
The **Taxi Ride** dataset contains over 100 million records and 23 different fields as follows:
* Trip ID
* Taxi ID
* Trip Start Timestamp
* Trip End Timestamp
* Trip Seconds
* Trip Miles
* Pickup Census Tract
* Pickup Community Area
* Drop-off Census Tract
* Drop-off Community Area
* Fare
* Tips
* Tolls
* Extras
* Trip Total
* Payment Type
* Company
* Pickup Centroid Latitude
* Pickup Centroid Longitude
* Pickup Centroid Location
* Drop-off Centroid Latitude
* Drop-off Centroid Longitude
* Drop-off Centroid Location
* Community Areas

Some cleanup has already been done, but more EDA effort will certainly be needed.  
*I am not planning to use all of the data, but potentially take a subset of it, to begin with.*  
More information about the **taxi ride** dataset can be found [here](https://digital.cityofchicago.org/index.php/chicago-taxi-data-released/).

The **Weather dataset** contains daily precipitation, snowfall, snow depth, maximum / minimum temperatures and flag for weather tags (such as thunder, heavy fog, tornado, etc.).  
More information about **weather** dataset can found [here](https://www.ncdc.noaa.gov/).

I will also need a helper dataset that would help to convert addresses into lat/long coordinates.

### Approach
The general plan is to get the data into postgreSQL database on AWS, clean & massage it, form one dataset (combined taxi ride and weather info) and train a multiple linear regression model.  
*Depending on the results, I'll have to try out other modelling techniques.*

#### Plan of Action
1. Get the data using City of Chicago API
2. Store the information in a postgreSQL database on AWS
3. Do thorough analysis of the data
4. Take appropriate cleaning steps (including dummification):
    * Calculate base rate (rate - tip) for credit card transactions
5. Find the links between taxi ride dataset and weather dataset
6. Do the train-test split (set aside test set)
7. Scale the data before modelling
8. Run a CV search for the best model and parameters
9. Get Cross-Validation scores for the best model
10. Examine the learning curve and train the model with more data, if needed
11. Test the model on the test dataset and assess the results
12. Summarize the findings
13. Build the presentation
14. Practice, practice, practice

### Known Unknowns
* If the relationship between my features and target is linear
* If weather data will have a significant effect on the ETA or the Rate
