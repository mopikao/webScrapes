import feedparser
from datetime import datetime
# https://github.com/martinmeinke/MMM-display-text-file

now = datetime.now()
dt_string = now.strftime("%d/%m %H:%M")
print("Updated at "+dt_string)

urls = ['https://www.straitstimes.com/news/singapore/rss.xml',
        'https://www.straitstimes.com/news/world/rss.xml'
    ]

for url in urls:
    feeds=[]
    feeds = feedparser.parse(url)['entries']
    #print(feeds)
    lengthFeed = len(feeds[0])
    #print(lengthFeed)

    for i in range(lengthFeed):
        print("☉ " + feeds[i]['title'])