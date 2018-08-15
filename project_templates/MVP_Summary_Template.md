## Student Grade Classification

### Problem:
Classifying students' grades into Pass / Fail

#### Description:
Predicting student's mathematics and Portuguese language grade based on various features, such as:
sex, age, relationship status, alcohol consumption, etc. In total 30 different features are available, appropriate ones will be selected using data analysis.

### Why?
Understanding how different characteristics, family situations and choices in life affect student's learning (through grades) can be very powerful. Especially when talking about youth education. If more schools did such data collection and analysis, we would likely have a much better education programs catered to different groups of students.
Moreover, actual science based information could be passed on to the parents who could, in turn, make smarter decisions for their children / teenagers.

Overall, This is not so much of a business problem, but rather a social responsibility question.  

### About The Dataset

**Number of datasets:** 2  
**Format**: CSV  
**Total observations:** 395 + 649  
**Missing values:** N/A  
**Dataset makeup:** 33 variables: 9 categorical, 8 boolean, 10 encoded, 6 numerical  
**Target variable (label):** Transformed G3 (final grade) (Pass / Fail)  
**Features to be excluded:** G1 and G2 (first and second semester grades)  
**Added features:** Grade type (Maths / Portuguese)  
**Dummified features:** 6  
**Number of features remaining:** 15  

[Data source](http://archive.ics.uci.edu/ml/datasets/Student+Performance#)
![What a Fail!](Student_Grades_dataset.png)

### Known Unknowns

* What relationship does alcohol consumption have with student's grades?
* What impact does being in a relationship have on student's grades?
* Is there a difference between the impact features have on math grades versus those of language skills (Portuguese)?
* How features like alcohol consumption correlate with age or relationship status?
* How does the family size or parent cohabitation impact student's grades?
* What relationship do extra-curricular activities have with alcohol consumption?
* Many more...

### Feedback
**- What is your *minimum* viable product? What are you simplifying in your model as a first iteration?**   
*My minimum viable product is predicting a Fail or Pass, using the two datasets*   
**- What is the label you are trying to predict?**   
*I will be transforming the G3 (Final grade column) into Pass / Fail and predicting that*   
**- It looks like there are encoded values in your data, e.g., `famsize=GT3` do you have a dictionary lookup of what these actually mean?**   
*Yes, I have a dictionary for all the values at the location where I got the datasets*   
**- How many observations are in the dataset?**   
*There are 395 observations for math score and another 649 for Portuguese score. I will be combining the two datasets*   
**- What is the age range of the students?**   
*The age range is 15 to 22*   
**- Do you have any information in the data regarding when they started drinking or dating?**   
*No, just how much they drink per weekday and per weekend (on the scale from 0 to 5)*   
**- It is likely you will have to group certain similar professions together to reduce the number of categorical values in the data.**   
*I won't be using all the features in my modelling, but I will only know which ones I'll use after the analysis*   
**- You have very few "real" numerical features to work with. Explore the data and make reasonable assumptions on which columns have hard numbers and which have been encoded to some numerical value.**   
*Do I have to have many numerical values? Is having encoded / dummified variables an issue? What could my problems be if I use many encoded values and only 2 or 3 numerical ones?*  

### Data analysis

* Figured out the hyper-parameters for 7 different models :thumbsup:  
  1. K-Nearest Neighbors (KNN)
  2. Logistic Regression
  3. Random Forest
  4. Naive Bayes (Gaussian)
  5. Naive Bayes (Bernoulli)
  6. Support Vector Classifier (SVC)
  7. Stochastic Gradient Descent (SGD)

* Compared all the models with their best hyper-parameters (Random Forest did the best on Cross Validation comparing AUC score and second best in precision) :thumbsup:  
* Random Forest was showing signs of overfitting initially, but after adding min_samples_leaf limit to 3, the score improved.  
* Need to do forward feature selection (**15 features left**) :thumbsup:
  1. Failures
  2. Discipline
  3. Absences
  4. Going out
  5. Willingness to Pursue Higher Education
  6. Father's education
  7. Studying time
  8. Family relationship
  9. Weekend alcohol consumption
  10. Mother's education
  11. Health
  12. Free time
  13. Age
  14. Whether paying for school or not
  15. Living in the city or not
* Oversamping (using Random, SMOTE and ADASYN) did not help (proved with Random Forest and Naive Bayes (Bernoulli)) :thumbsdown: :confused:
* Final precision score on the test set was **~0.86**, final AUC score was **~0.67**   
### The final analysis has shown that:
  1. As the Study Time increases, ceteris paribus, so does the probability to Pass, but it does so with diminishing returns  
  2. As the previous failures increase, ceteris paribus, the probability to Pass drops dramatically  
  3. The better educated are student's parents, the more likely they are to Pass  
  4. The most interesting finding was that the probability to Pass peaks at the average level of Free Time / Going Out / Weekend Alcohol consumption, ceteris paribus
