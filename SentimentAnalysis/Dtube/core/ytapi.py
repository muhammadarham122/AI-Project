import os
import googleapiclient.discovery
from apiclient.discovery import build


api_key = "AIzaSyABHi5bRfhQHz3XzPIUCu-u_O0h1LZpPbM"

yt = build('youtube', 'v3', developerKey=api_key)

# req = yt.search().list(part='snippet', q='django', type='video')https://www.youtube.com/watch?v=Nr-gYadj5dw
req1 = yt.commentThreads().list(part='snippet', moderationStatus="published",
                                order="relevance",
                                textFormat="plainText",
                                videoId="Nr-gYadj5dw")
res = req1.execute()
print(res)
bag = []
for item in res['items']:
    comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
    print(comment)
    bag.append(comment)
    print(bag)

# res(['items']['snippet']['topLevelComment']['snippet']['textDisplay'])
