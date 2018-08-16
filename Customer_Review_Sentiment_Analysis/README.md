## Customer Review Sentiment Analysis

### Problem:
Proactive Customer Churn Management

#### Description:
Analyze customer reviews, assign a sentiment (and a confidence score) and cluster them into 5-10 categories (food, legroom, delays, etc.)

### Why?
Customer churn is often an overlooked metric in a sales oriented organization, which, in my opinion, is a big mistake. Landing a new customer consumes much more resources and time than retaining an existing customer would. Therefore, with this project I intend to explore ways to decrease customer churn using NLP and unsupervised learning techniques.


### Plan of Action
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

### About The Dataset:

**Number of datasets:** 1  
**Format**: csv / SQLite database   
**Total observations:** 14,640   
**Missing values:** None  
**Dataset makeup:** A column with the tweet (text), Airline column  
**Target variable (label):** sentiment, category  
**Features to be excluded:** airline_sentiment,	airline_sentiment_confidence,	negativereason,	negativereason_confidence,	airline_sentiment_gold  
**Added features:** None  
**Dummified features:** None  

### Known Unknowns
* Number of categories
* The distribution of the sentiments (potentially mostly negative)
* Could airline be used for clustering?
* Can I interpret emojis in my NLP analysis?

### Data analysis


### Final Conclusions


### Random stuff
