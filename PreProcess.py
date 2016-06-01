import datetime
import ast
import pandas as pd
#import lda
import json
import gensim
import re
import glob, os
import numpy as np
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import matplotlib.pyplot as plt
from gensim import corpora, models
#en_stop = get_stop_words('en')
from sklearn import preprocessing
import unicodedata
operators = set(('Ive'))
cachedStopWords = set(stopwords.words("english")) + operators


tokenizer = RegexpTokenizer(r'\w+')
p_stemmer = PorterStemmer()
from openpyxl import Workbook

class PreProcess:
    def __init__(self,file_path,file_name):
        self.dir = file_path
        self.name = file_name
        self.corpus = []

    def returnInt(self,input):
        if(input != "n/a"):
            return int(input)
        else:
            return -1
    def unicodeToString(self,input):
        return unicodedata.normalize('NFKD', input).encode('ascii','ignore')

    def loadToDataFrame(self):
        reading_dic = {1:self.unicodeToString,2: self.returnInt,3: self.returnInt,4: self.returnInt,5: self.returnInt
                       ,7: self.returnInt}
        data = pd.read_excel(self.dir + self.name, converters=reading_dic)
        data.columns = ["id","comment","recommendation","shopping_experience",
                        "choice_shops","choice_catering"
                        , "shopping_spend", "catering_spend"]
        data = data[data.comment != "None" ]
        data = data[data.comment != "See Raw Data" ]
        data = data[data.comment != "See raw data" ]
        data.replace(to_replace=-1, value=np.nan, inplace=True, regex=True)
        #pd.to_numeric(data.recommendation,errors='coerce')
        data = data.convert_objects(convert_numeric=True)
        #data.comment.toString()
        print(type(data.comment.ix[1]))
        return data

    def removeSingleChars(subject):
        result = []
        for i in subject:
            if(len(i)>2):
                result.append(i)
        return result

    def removeNonLatin(subject):
        result = re.sub(r"[^\x00-\x7F]+","", subject)
        return result

    def initialProcess(self):
        data = self.loadToDataFrame()
        for i in range(0,len(data)):
            raw_doc = self.removeNonLatin(data.comment.ix[i].lower())
            tokens = tokenizer.tokenize(raw_doc)
            stopped_tokens = [i for i in tokens if not i in cachedStopWords]
            stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
            self.corpus.append(self.removeSingleChars(stemmed_tokens))


PreProcess("/Users/eirinimilaiou/Documents/ucl/CACI/test_data/","Example_Data.xlsx").loadToDataFrame()

