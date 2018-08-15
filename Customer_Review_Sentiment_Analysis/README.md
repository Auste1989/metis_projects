## Customer Review Sentiment Analysis

### Problem:
Proactive Customer Churn Management

#### Description:
Analyze customer reviews, assign a sentiment (and a confidence score) and cluster them into 5-10 categories (food, legroom, delays, etc.)

### Why?
Customer churn is often an overlooked metric in a sales oriented organization, which, in my opinion, is a big mistake. Landing a new customer consumes much more resources and time than retaining an existing customer would. Therefore, with this project I intend to explore ways to decrease customer churn using NLP and unsupervised learning techniques.


### Plan of Action


### About The Dataset:

**Number of datasets:** 1  
**Format**: csv / SQLite database   
**Total observations:** 14,640   
**Missing values:**   
**Dataset makeup:**   
**Target variable (label):**   
**Features to be excluded:**   
**Added features:**   
**Dummified features:**   
**Dropped features after Random Forest analysis:**  

### Known Unknowns
* Number of categories
* The distribution of the sentiments (potentially mostly negative)
* Could airline be used for clustering?
* Can I interpret emojis in my NLP analysis?

### Data analysis


### Final Conclusions


### Random stuff
*this will be useful*
import os

class MySentences(object):
    # a memory-friendly way to load a large corpora
     def __init__(self, dirname):
            self.dirname = dirname

     def __iter__(self):
        # iterate through all file names in our directory
         for fname in os.listdir(self.dirname):
                for line in open(os.path.join(self.dirname, fname), encoding="ISO-8859-1"):
                    word=line.lower().split()
                    if word not in stop:
                        yield word

sentences = MySentences('data/gutenberg')
model = gensim.models.Word2Vec(sentences,size=100,min_count=3,workers=4)
