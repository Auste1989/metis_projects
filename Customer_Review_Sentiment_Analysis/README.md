## Customer Service Action Recommender

### Problem:

#### Description:


### Why?


### Plan of Action


### About The Dataset:

**Number of datasets:**  
**Format**:   
**Total observations:**   
**Missing values:**   
**Dataset makeup:**   
**Target variable (label):**   
**Features to be excluded:**   
**Added features:**   
**Dummified features:**   
**Dropped features after Random Forest analysis:**  

### Known Unknowns


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
