'''
Sentiment Analysis of Youtube Video`s comments wit the help of
TextBlob that predict its negative or positive with the help of
Natural Language Processing (NLP)

Polarity - It simply means emotions expressed in a sentence.

Subjectivity - Subjective sentence expresses some personal feelings, views, or beliefs.
'''

from apiclient.discovery import build
from textblob.sentiments import PatternAnalyzer
from textblob import TextBlob
from bs4 import BeautifulSoup

import json
import re
import requests
import os
import googleapiclient.discovery


value = 'https://www.youtube.com/watch?v=HtZzIHSDhMM'

match1 = re.findall(r"(=\S+)", value)


for mat in match1:
    mat1 = ''
    # print(mat)
    # print(type(mat))
    mat1 = list(mat)

    mat1.remove("=")
    # print(type(mat1))
    # print(mat1)
    mat2 = ''.join(mat1)
    # print(type(mat2))
    # print(mat2)


api_key = "AIzaSyABHi5bRfhQHz3XzPIUCu-u_O0h1LZpPbM"
yt = build('youtube', 'v3', developerKey=api_key)

req1 = yt.commentThreads().list(part='snippet', moderationStatus="published",
                                order="relevance",
                                textFormat="plainText",
                                videoId=mat2)
res = req1.execute()
# print(res)
bags = []
for item in res['items']:
    comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
    # print(comment)
    bags.append(comment)
    comments = ''
    sentences = comments.join(bags)
    sentiment_analyzer = PatternAnalyzer()
    # print(sentences)
    # print(sentiment_analyzer.analyze(sentences))
    senti = sentiment_analyzer.analyze(sentences)
    # change the subjectivity and Polarity as per your liking in vv1
    sentis = senti.subjectivity
    print(sentis)
    if sentis < 0.5:
        print("The Comments Subjectivity are - Positive")
    else:
        print("The Comments Subjectivity are - Negative")
