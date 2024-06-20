from joblib import load
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import nltk
import re
import string
# nltk.download('stopwords')
# nltk.download('punkt')

def preprocessing(text):
    text = text.lower()
    text = re.sub('\[.*?\]','',text)
    text = re.sub("\\W"," ",text)
    text = re.sub('https?://\S+|www\.\S+','',text)
    text = re.sub('<.*?>+','',text)
    text = re.sub('[%s]' % re.escape(string.punctuation) ,'',text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*','',text)
    text = re.sub('[%s]' % re.escape(string.punctuation) ,'',text)  #Removes all punctuation characters using string.punctuation
    words = word_tokenize(text)                 #Tokenize the words
    stop_words = set(stopwords.words('english'))    #stores all stopwords in english as a set stop_words
    words = [word for word in words if word not in stop_words]  #remove stopwords
    stemmer = PorterStemmer()               #porterstemmer initializes to stemmer 
    words = [stemmer.stem(word) for word in words]  #stemming process
    text = ' '.join(words)                  #Joins all the words after stopwords removal and stemmming as a text
    return text

def predict_RF(data):
    data=np.array(data).reshape(-1)
    model=load(r"C:\Users\91628\Desktop\mini project\GUI_mini\myworld\Scripts\fakenews\app1\RF.pk1")
    data=pd.Series(data)
    data = data.apply(preprocessing)
    vectorization = load(r"C:\Users\91628\Desktop\mini project\GUI_mini\myworld\Scripts\fakenews\app1\f.joblib")
    data=vectorization.transform(data)
    result=model.predict(data)
    return result[0]
 
def predict_LG(data):
    data=np.array(data).reshape(-1)
    model=load(r'C:\Users\91628\Desktop\mini project\GUI_mini\myworld\Scripts\fakenews\app1\LR.pk1')
    data=pd.Series(data)
    data = data.apply(preprocessing)
    vectorization = load(r"C:\Users\91628\Desktop\mini project\GUI_mini\myworld\Scripts\fakenews\app1\f.joblib")
    data=vectorization.transform(data)
    result=model.predict(data)
    return result[0]

def predict_SVM(data):
    data=np.array(data).reshape(-1)
    model=load(r"C:\Users\91628\Desktop\mini project\GUI_mini\myworld\Scripts\fakenews\app1\SVM.pk1")
    data=pd.Series(data)
    data = data.apply(preprocessing)
    vectorization = load(r"C:\Users\91628\Desktop\mini project\GUI_mini\myworld\Scripts\fakenews\app1\f.joblib")
    data=vectorization.transform(data)
    result=model.predict(data)
    return result[0]

def predict_PAC(data):
    data=np.array(data).reshape(-1)
    model=load(r"C:\Users\91628\Desktop\mini project\GUI_mini\myworld\Scripts\fakenews\app1\PAC.pk1")
    data=pd.Series(data)
    data = data.apply(preprocessing)
    vectorization = load(r"C:\Users\91628\Desktop\mini project\GUI_mini\myworld\Scripts\fakenews\app1\f.joblib")
    data=vectorization.transform(data)
    result=model.predict(data)
    return result[0]

