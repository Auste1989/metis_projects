## Customer Service Sentiment Analysis

### Problem:
Proactive Customer Churn Management

#### Description:
Analyze customer reviews, assign a sentiment score and cluster them into 5-10 categories (food, space, delays, etc.)

### Why?
Customer churn is often an overlooked metric in a sales oriented organization, which, in my opinion, is a big mistake. Landing a new customer consumes much more resources and time than retaining an existing customer would. Therefore, with this project I intend to explore ways to decrease customer churn using NLP and unsupervised learning techniques.

### About The Dataset
I initially thought of using EXCITEMENT (Kotlerman et al, 2015) dataset containing customers reviews of railway services. However, I discovered that the dataset only contained 400 records, which is way too small for this project.
I am now looking for an, ideally, transportation related reviews dataset, I found a Twitter dataset on US airline reviews with around 15,000 records. I will use it, if I can't find anything better.

### Approach
My approach would be to first identify the sentiment of the review (tweet) and then cluster the reviews into categories, that would eventually result in actionable insights (recommendations). *Recommendation system is not part of my MVP*

### Known Unknowns
* Number of categories
* The distribution of the sentiments (potentially mostly negative)
* 

### Data analysis
