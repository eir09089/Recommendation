import datetime
import ast
import pandas as pd
import lda
import json
import gensim
import re
import glob, os
import numpy as np
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
import matplotlib.pyplot as plt
from gensim import corpora, models
en_stop = get_stop_words('en')
tokenizer = RegexpTokenizer(r'\w+')
p_stemmer = PorterStemmer()
from openpyxl import Workbook

class PreProcess:
    def __init__(self,file_path,file_name):
        self.dir = file_path
        self.name = file_name

    def loadToDataFrame(self):
        file = open(self.dir+self.name, "r" , encoding="utf8")
