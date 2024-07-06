import nltk
nltk.download("wordnet")
from nltk.stem import LancasterStemmer
from nltk.stem import WordNetLemmatizer
from sklearn.base import BaseEstimator, TransformerMixin
from nltk.corpus import stopwords
import re

class process_raw_strings(BaseEstimator, TransformerMixin):
    def __init__(self, stopwords=False):
        self.lnc_stem = LancasterStemmer()
        self.lemma = WordNetLemmatizer()
        self.stopwords = stopwords.words("english")
        if stopwords:
            self.stopwords = list(set(self.stopwords + stopwords))

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        process_documents = []
        for msg in X:
            msg = msg.lower()
            msg = re.sub(r"[!\"#$%&\'()*+,-./:;<=>?@[\\\]^_`{|}~)]", "", msg)
            sentence = []
            for words in msg.split():
                if words not in self.stopwords:
                    lemitize = self.lemma.lemmatize(words)
                    stem = self.lnc_stem.stem(lemitize)
                    sentence.append(words)
            msg = " ".join(sentence)
            process_documents.append(msg)

        return process_documents
