## Customer Review Sentiment Analysis

### Problem:
Proactive Customer Churn Management

#### Description:
Analyze customer reviews, assign a sentiment (and a confidence score) and cluster them into 5-10 categories (food, legroom, delays, etc.)

### Why?
Customer churn is often an overlooked metric in a sales oriented organization, which, in my opinion, is a big mistake. Landing a new customer consumes much more resources and time than retaining an existing customer would. Therefore, with this project I intend to explore ways to decrease customer churn using NLP and unsupervised learning techniques.

### Plan of Action
1. Explore the datasets :thumbsup:
2. Set aside a test set :thumbsup:
3. Use TextBlob / Vader / external APIs for sentiment analysis and confidence score :thumbsup:
4. Store the results of the sentiment analysis in a separate column :thumbsup:
5. Clean up the data in pandas :thumbsup:  
      **Removed the following text items:**
      * all "@" sign preceding text
      * hashtags
      * codes and numbers
      * urls
      * locations
      * months
      * emojis
      * airport codes
6. Pickle the clean training dataset :thumbsup:
7. Filter only on negative tweets :thumbsup:
8. Process the words to lemmatize and singularize :thumbsup:
9. Use CountVectorizer and TF-IDF to vectorize my data (exclude stop words and punctuation) :thumbsup:
  * Look into vectorizing emojis ***decided not to for MVP***
10. Do dimensionality reduction (tried LSA, NMF, PCA and LDA) :thumbsup:
    * TF-IDF with LDA initially seemed to work best, but after using tSNE to plot, I noticed that Count Vectorizer with NMF technique produced clearer topics, so I settled with Count Vectorizer + NMF model :wink:
11. Cluster negative tweets into categories  
    * KMeans generated a good result, so trying other clustering techniques wasn't necessary. :smirk:
12. Use T-SNE to plot the results :thumbsup:
13. Name the clusters :thumbsup:
14. Assign an action to each category :relieved:
15. Write a recommendation function to advice an action based on the cluster the tweet falls into :blush:
16. Test the model on my test dataset and assess the results :thumbsup:
17. Create the presentation
18. Practice, practice, practice :smirk:

### About The Dataset:

**Number of datasets:** 1  
**Format**: csv / SQLite database   
**Total observations:** 14,885  
**Missing values:** None  
**Dataset makeup:** A column with the tweet (text), Airline column  
**Target variable (label):** sentiment, category  
**Features to be excluded:** airline_sentiment,	airline_sentiment_confidence,	negativereason,	negativereason_confidence,	airline_sentiment_gold  
**Added features:** None  
**Dummified features:** None  

### Known Unknowns
* Number of categories :ballot_box_with_check:
* The distribution of the sentiments (potentially mostly negative) ***The distribution was pretty even***
* Could airline be used for clustering? ***Didn't explore***
* Can I interpret emojis in my NLP analysis? ***Wasn't needed***

### Final Conclusions
* The model was able to do pretty decent sentiment analysis, especially for negative tweets
* It identified Customer Service, Baggage Loss and Missed Connection mentioning tweets pretty accurately
* It is very bad at identifying sarcasm
