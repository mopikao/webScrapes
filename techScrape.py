#!/usr/bin/python

import feedparser
from datetime import datetime
# https://github.com/SaltyRiver/MMM-SimpleText
# https://github.com/martinmeinke/MMM-display-text-file

now = datetime.now()
dt_string = now.strftime("%d/%m %H:%M")
print("Updated at "+dt_string)

urls = ['http://feeds2.feedburner.com/thenextweb',
        'https://gizmodo.com/rss'

    ]

textFile = open("techText.txt","w",encoding="utf-8")
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