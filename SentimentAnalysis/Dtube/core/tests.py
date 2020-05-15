# from django.test import TestCase

from apiclient.discovery import build
from textblob.sentiments import PatternAnalyzer
from textblob import TextBlob
from bs4 import BeautifulSoup

import json
import re
import requests
import os
import googleapiclient.discovery


# s = '{"cardinality":483,"timestamp":15369087280,"deltas":{"week_over_week":{"delta_fraction":0.047722318876,"last_week_value":146}}}'
# print('Active: %s' % json.loads(s)['cardinality'])

# match1 = re.finditer(r"v=*", value)
# match1 = re.finditer(r"\wv=", value)
# value = 'https://www.youtube.com/watch?v=2ZH8kRfg-zs'
# match1 = re.partition("v=", value)
# print(type(mat1))
# mat = mat1
# match = re.match(r"https://www.youtube.com/watch\?v=\w", value)

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
    vv = sentiment_analyzer.analyze(sentences)
    vv1 = vv.polarity
    # print(vv1)
    if vv1 > 0.5:
        print("Positive")

    # print(bags)
    # if bags == item.values():
    #     # print(bags['textDisplay'])
    #     comments = ''
    #     sentences = comments.join(bags)
    #     print(sentences)
    #     sentiment_analyzer = PatternAnalyzer()
    #     print(sentiment_analyzer.analyze(sentences))
    # blob = TextBlob(sentences)
    # for sentence in blob.sentences:
    #     print(sentence.sentiment)

    # dicttt = {'kind': 'youtube#commentThreadListResponse',
    #           'etag': '"Dn5xIderbhAnUk5TAW0qkFFir0M/U6sxaWDmx3WJSkOune2IUd1CCLY"',
    #           'pageInfo': {'totalResults': 2, 'resultsPerPage': 20},
    #           'items': [{'kind': 'youtube#commentThread',
    #                      'etag': '"Dn5xIderbhAnUk5TAW0qkFFir0M/DOZqvtoG6uvBlHRbRJstDFz2rFQ"',
    #                      'id': 'Ugx51L5YtDrNaT7XBnp4AaABAg',
    #                      'snippet': {'videoId': 'HtZzIHSDhMM',
    #                                  'topLevelComment': {'kind': 'youtube#comment',
    #                                                      'etag': '"Dn5xIderbhAnUk5TAW0qkFFir0M/lbY8Z8A3xmaNGIGMDhWCikvEo_U"',
    #                                                      'id': 'Ugx51L5YtDrNaT7XBnp4AaABAg',
    #                                                      'snippet': {'authorDisplayName': 'Mubashar Mehmood',
    #                                                                  'authorProfileImageUrl': 'https://yt3.ggpht.com/a/AATXAJy5HF051b4ES5StS5aOUSoxdrP-AgPebAbbHQ=s48-c-k-c0xffffffff-no-rj-mo',
    #                                                                  'authorChannelUrl': 'http://www.youtube.com/channel/UCxKgLUXEDx_5RTK9gGLWWxQ',
    #                                                                  'authorChannelId': {'value': 'UCxKgLUXEDx_5RTK9gGLWWxQ'},
    #                                                                  'videoId': 'HtZzIHSDhMM',
    #                                                                  'textDisplay': 'Amazing tutorial, Can you tell me how can i extract functions name from file and check in which classes functions are called?',
    #                                                                  'textOriginal': 'Amazing tutorial, Can you tell me how can i extract functions name from file and check in which classes functions are called?',
    #                                                                  'canRate': True, 'viewerRating': 'none',
    #                                                                  'likeCount': 0,
    #                                                                  'publishedAt': '2020-01-11T13:37:19.000Z',
    #                                                                  'updatedAt': '2020-01-11T13:46:45.000Z'}},
    #                                  'canReply': True,
    #                                  'totalReplyCount': 0,
    #                                  'isPublic': True}},
    #                     {'kind': 'youtube#commentThread',
    #                      'etag': '"Dn5xIderbhAnUk5TAW0qkFFir0M/Ve_u7-p9Jbfd8ViIfafsBdItV8U"',
    #                      'id': 'UgzCNmiqWHoDOAygqQB4AaABAg',
    #                      'snippet': {'videoId': 'HtZzIHSDhMM',
    #                                  'topLevelComment': {'kind': 'youtube#comment',
    #                                                      'etag': '"Dn5xIderbhAnUk5TAW0qkFFir0M/EmRib_yS92WhpfGW474TTuFW7tE"',
    #                                                      'id': 'UgzCNmiqWHoDOAygqQB4AaABAg',
    #                                                      'snippet': {'authorDisplayName': 'Sudarsana Shankar',
    #                                                                  'authorProfileImageUrl': 'https://yt3.ggpht.com/a/AATXAJx8HhG2RdpHBLBGU2RitZj3cE48W6ytlTE89A=s48-c-k-c0xffffffff-no-rj-mo',
    #                                                                  'authorChannelUrl': 'http://www.youtube.com/channel/UCNA-xubJ8jazUkeBpok7dtQ',
    #                                                                  'authorChannelId':
    #                                                                  {'value': 'UCNA-xubJ8jazUkeBpok7dtQ'},
    #                                                                  'videoId': 'HtZzIHSDhMM',
    #                                                                  'textDisplay': 'Very good video.. Thanks for sharing.. It saved me lot of time while I was trying to accomplish the same.. Can you suggest any good resource(book/link) to learn to write Regular Expressions easily and efficiently well ?', 'textOriginal': 'Very good video.. Thanks for sharing.. It saved me lot of time while I was trying to accomplish the same.. Can you suggest any good resource(book/link) to learn to write Regular Expressions easily and efficiently well ?',
    #                                                                  'canRate': True,
    #                                                                  'viewerRating': 'none',
    #                                                                  'likeCount': 0,
    #                                                                  'publishedAt': '2019-08-01T11: 12: 34.000Z',
    #                                                                  'updatedAt': '2019-08-01T11: 12: 34.000Z'}},
    #                                  'canReply': True,
    #                                  'totalReplyCount': 0,
    #                                  'isPublic': True}
    #                      }
    #                     ]
    #           }

    # dict = {'kind': 'youtube#commentThreadListResponse',
    #         'etag': 'Dn5xIderbhAnUk5TAW0qkFFir0M/U6sxaWDmx3WJSkOune2IUd1CCLY',
    #         'pageInfo': {'totalResults': 2, 'resultsPerPage': 20},
    #         'items': [{'kind': 'youtube#commentThread',
    #                    'etag': '"Dn5xIderbhAnUk5TAW0qkFFir0M/DOZqvtoG6uvBlHRbRJstDFz2rFQ"',
    #                    'id': 'Ugx51L5YtDrNaT7XBnp4AaABAg',
    #                    'snippet': {'videoId': 'HtZzIHSDhMM',
    #                                'topLevelComment': {'kind': 'youtube#comment',
    #                                                    'etag': '"Dn5xIderbhAnUk5TAW0qkFFir0M/lbY8Z8A3xmaNGIGMDhWCikvEo_U"',
    #                                                    'id': 'Ugx51L5YtDrNaT7XBnp4AaABAg'}}}]}
    # sentiment_analyzer = PatternAnalyzer()
    # print(sentiment_analyzer.analyze('This is really good'))

    # for key, values in dicttt.items():
    #     # print(key, values)
    #     if type(values) is dicttt:
    #         print(key, ":", values)
    #         sentiment_analyzer = PatternAnalyzer()
    #         print(sentiment_analyzer.analyze(key, values))

    # print(key, ":", values)

    #  print(values)
    #     else:

 #         api_key = "AIzaSyABHi5bRfhQHz3XzPIUCu-u_O0h1LZpPbM"
    #         yt = build('youtube', 'v3', developerKey=api_key)

    #         req1 = yt.commentThreads().list(part='snippet', moderationStatus="published",
    #                                         order="relevance",
    #                                         textFormat="plainText",
    #                                         videoId="Nr-gYadj5dw")
    #         res = req1.execute()
    #         print(res)
    #         bag = []
    #         for item in res['items']:
    #             comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
    #             print(comment)
    #             bag.append(comment)
    #         print(bag)

    # value = 'https://www.youtube.com/watch?v=HtZzIHSDhMM'

 # mdl = joblib.load(
        #     "D:/AI Project/SentimentAnalysis/Dtube/core/trainedmodel.pkl")
        # mdl.predictions(bag)
        # print(mdl)
