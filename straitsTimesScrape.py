#!/usr/bin/python

import feedparser
from datetime import datetime
# https://github.com/martinmeinke/MMM-display-text-file

now = datetime.now()
dt_string = now.strftime("%d/%m %H:%M")
print("Updated at "+dt_string)

urls = ['https://www.straitstimes.com/news/singapore/rss.xml',
        'https://www.straitstimes.com/news/world/rss.xml'
    ]

textFile = open("straitsTimes.txt","w",encoding="utf-8")
textFile.write("Updated at "+ dt_string + "\n")

for url in urls:
    textFile.write("\n")
    feeds=[]
    feeds = feedparser.parse(url)['entries']
    #print(feeds)
    lengthFeed = len(feeds)

    if lengthFeed > 10:
        lengthFeed = 10

    #print(lengthFeed)

    for i in range(lengthFeed):
        print("☉ " + feeds[i]['title'])
        textFile.write("☉ " + feeds[i]['title'] + "\n")

textFile.close()