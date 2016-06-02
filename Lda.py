import pandas as pd
import gensim
import re
import glob, os
import numpy as np
from gensim.models import LdaModel
from gensim import corpora, models
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import matplotlib.pyplot as plt

class Lda:
    def __init__(self,docs):
        self.docs = docs
        self.path_mallet = "/Users/eirinimilaiou/Documents/ucl/CACI/codes/mallet-2.0.7/bin/mallet"
        self.corpus = []
        self.dictionary = []

    def corpus_create(self):
        self.dictionary = corpora.Dictionary(self.docs)
        self.corpus = [self.dictionary.doc2bow(text) for text in self.docs]

    def model_create(self,num_top,model_type):
        self.corpus_create()
        if(model_type == "gensim"):
            ldamodel = gensim.models.ldamodel.LdaModel(self.corpus, num_topics=num_top, id2word = self.dictionary,
                                                   passes=20,minimum_probability=0.00)
            return ldamodel
        else:
            ldaMallet = gensim.models.wrappers.LdaMallet(self.path_mallet
                                             ,corpus=self.corpus,num_topics = num_top,id2word=self.dictionary)
            return ldaMallet

    def model_results(self,num_top,model_type):
        ldaModel = self.model_create(num_top,model_type)
        ldaModel.print_topics(num_top,5)


