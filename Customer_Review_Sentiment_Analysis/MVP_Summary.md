## Customer Review Sentiment Analysis

### Problem:
Proactive Customer Churn Management

#### Description:
Analyze customer reviews, assign a sentiment (and a confidence score) and cluster them into 5-10 categories (food, legroom, delays, etc.)

### Why?
Customer churn is often an overlooked metric in a sales oriented organization, which, in my opinion, is a big mistake. Landing a new customer consumes much more resources and time than retaining an existing customer would. Therefore, with this project I intend to explore ways to decrease customer churn using NLP and unsupervised learning techniques.

### About The Dataset
I initially thought of using EXCITEMENT (Kotlerman et al, 2015) dataset containing customers reviews of railway services. However, I discovered that the dataset only contained 400 records, which is way too small for this project.
I am now looking for an, ideally, transportation related reviews dataset, I found a Twitter dataset on US airline reviews with around 15,000 records. I will use it, if I can't find anything better.
I got the Twitter dataset from Kaggle.

### Approach
My approach would be to first identify the sentiment of the review (tweet) and then cluster the reviews into categories, that would eventually result in actionable insights (recommendations). *Recommendation system is not part of my MVP*  
I am planning to store my data either in mongodb or SQL database (SQLite database for this is available on Kaggle).
I have not had a chance to think about the techniques I will use.

#### Plan of Action
1. Explore the datasets
2. Clean up the data in pandas
3. Store the information either in my own SQL database
4. Set aside a test set
5. Use CountVectorizer and TF-IDF to vectorize my data (exclude stop words and punctuation)
  * Look into vectorizing emojis
6. Use TextBlob for sentiment analysis and confidence score
7. Store the results of the sentiment analysis in a separate column
8. Filter only on negative tweets
9. Do dimensionality reduction (try LSA, NMF and LDA)
10. Cluster negative tweets into categories (use T-SNE to plot the results)
11. Assign an action to each category
12. Write a recommendation function to advice an action based on the cluster the tweet falls into
13. Test the model on my test dataset and assess the results
14. Summarize the findings
15. If time allows, generate recommendations based on review category
16. Build the presentation
17. Practice, practice, practice

### Known Unknowns
* Number of categories
* The distribution of the sentiments (potentially mostly negative)
* Could airline be used for clustering?
* Can I interpret emojis in my NLP analysis?

### Data analysis

TBD
