from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages


import pickle
from tensorflow.keras import backend as K

import joblib
import numpy as np
from sklearn import preprocessing
import pandas as pd

from .forms import Form
from django.views.generic.edit import FormView
import os
import googleapiclient.discovery
from apiclient.discovery import build
import json
import re
import nltk
from textblob.sentiments import PatternAnalyzer
from textblob import TextBlob


def trainer(request):
    pass


# def searchLink(link):
#     # def searchName(searchterm):
#     match1 = re.findall(r"(=\S+)", link)
#     # print(match1)

#     for mat in match1:
#         mat1 = ''
#         # print(mat)
#         # print(type(mat))
#         mat1 = list(mat)

#         mat1.remove("=")
#         # print(type(mat1))
#         # print(mat1)
#         mat2 = ''.join(mat1)
#         # print(type(mat2))
#         # print(mat2)

#         api_key = "AIzaSyABHi5bRfhQHz3XzPIUCu-u_O0h1LZpPbM"
#         yt = build('youtube', 'v3', developerKey=api_key)

#         req1 = yt.commentThreads().list(part='snippet', moderationStatus="published",
#                                         order="relevance",
#                                         textFormat="plainText",
#                                         videoId=mat2)
#         res = req1.execute()
#         # print(res)

#         for item in res['items']:
#             bags = []
#             comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
#             # print(comment)
#             bags.append(comment)
#             comments = ''
#             sentences = comments.join(bags)
#             sentiment_analyzer = PatternAnalyzer()
#             # print(sentences)
#             # print(sentiment_analyzer.analyze(sentences))
#             vv = sentiment_analyzer.analyze(sentences)
#             vv1 = vv.polarity
#             # print(vv1)
#             if vv1 > 0.5:
#                 print("Positive")


def home(request):
    if request.method == 'GET':
        form = Form()
        if form.is_valid():
            link = request.GET.get('')

            for mat in match1:
                mat1 = ''
                print(mat)
                print(type(mat))
                mat1 = list(mat)

                mat1.remove("=")
                # print(type(mat1))
                # print(mat1)
                mat2 = ''.join(mat1)
                # print(type(mat2))
                # print(mat2)

            # api_key = "AIzaSyABHi5bRfhQHz3XzPIUCu-u_O0h1LZpPbM"
            # yt = build('youtube', 'v3', developerKey=api_key)

            # req1 = yt.commentThreads().list(part='snippet', moderationStatus="published",
            #                                 order="relevance",
            #                                 textFormat="plainText",
            #                                 videoId=mat2)
            # res = req1.execute()
            # print(res)
            # bags = []
            # for item in res['items']:
            #     comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            #     # print(comment)
            #     bags.append(comment)
            #     comments = ''
            #     sentences = comments.join(bags)
            context = {
                'form': form,
                'data': vv1
            }

    else:
        form = Form()
        link = request.GET.get('')
        for mat in match1:
            mat1 = ''
            print(mat)
            print(type(mat))
            mat1 = list(mat)

            mat1.remove("=")
            # print(type(mat1))
            # print(mat1)
            mat2 = ''.join(mat1)
            # print(type(mat2))
            # print(mat2)
        # print(link)
    context = {
        'form': form
    }

    return render(request, 'form/home.html', context)
