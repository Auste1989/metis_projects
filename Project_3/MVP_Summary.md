## Minimal Viable Product (MVP) Summary

### Problem:
Classifying students' grades into Pass / Fail

#### Description:
Predicting student's mathematics and Portuguese language grade based on different features, such as:
sex, age, relationship status, alcohol consumption, etc. In total 30 different features are available, appropriate ones will be selected using data analysis.

### Why?
I have a *(strong)* opinion that drinking alcohol has a negative impact on learning. It would be interesting to see if that is, indeed, the case in a more scientific way rather than just from personal experience. This is not so much of a business problem rather than a social responsibility question.  
*In terms of domain knowledge, I don't have any specific knowledge other than my, my family's and friends' experience*

### Plan of Action:

1. Clearly define the question - :thumbsup:
2. Get a good quality dataset (ideally multiple) - :thumbsup:
3. Explore and Analyse the dataset(s)
4. Clean missing values, outliers (if any) and obvious mistakes
5. Transform the variables (dummify, etc.)
6. Store the data in an SQL database
7. Select the features
8. Model using different models (KNN, Logistic Regression, Decision Trees, Random Forest, etc.)
9. Refine feature selectetion and repeat above step
10. Verify which model performs the best and finalize it
11. Create online interface using Flask
12. Visualize the results
13. Create the presentation
14. This time actually practice presenting

### Dataset

![What a Fail!]('Student_Grades_dataset.png')

| Sex | Age | Relationship Status | Weekday Alcohol Consumption | Weekend Alcohol Consumption | Final Grade |   
| --- | --- | --- | --- | --- | --- |   
| 1 | 14 | 1 | 2 | 0 | Pass |   
| 0 | 17 | 1 | 0 | 4 | Fail |   

### Currently no Known Unknowns
