# import youtube_sentiment as yt
# print(yt)
# # yt.video_summary( < 'AIzaSyABHi5bRfhQHz3XzPIUCu-u_O0h1LZpPbM' > , < Youtube Video ID > , < Max Pages of Comments > , < Sentiment Model > )

# yt.tagged_comments('AIzaSyABHi5bRfhQHz3XzPIUCu-u_O0h1LZpPbM',
#                    '-QMg39gK624',
#                    '2',
#                    'lr_sentiment_basic')

import os
import googleapiclient.discovery
from apiclient.discovery import build


api_key = "AIzaSyABHi5bRfhQHz3XzPIUCu-u_O0h1LZpPbM"

yt = build('youtube', 'v3', developerKey=api_key)

# req = yt.search().list(part='snippet', q='django', type='video')https://www.youtube.com/watch?v=Nr-gYadj5dw
req1 = yt.commentThreads().list(part='snippet', moderationStatus="published",
                                order="relevance",
                                textFormat="plainText",
                                videoId="HtZzIHSDhMM")
res = req1.execute()
print(res)
bag = []
for item in res['items']:
    comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
    print(comment)
    bag.append(comment)
    print(bag)

# res(['items']['snippet']['topLevelComment']['snippet']['textDisplay'])
