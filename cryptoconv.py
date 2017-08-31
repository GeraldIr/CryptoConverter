# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 22:10:21 2017

@author: Gerald Walter Irsiegler
"""
import praw
import os
import re
import json

import requests
import datetime

reddit = praw.Reddit('cryptoconv')
subreddit = reddit.subreddit("gerildtest")

supported = "(bch|btc|xmr|eth|etc|ltc|usd|eur)"
regtext = supported + " to " + supported
regex = re.compile(regtext)

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
       posts_replied_to = f.read()
       posts_replied_to = posts_replied_to.split("\n")
       posts_replied_to = list(filter(None, posts_replied_to))



for submission in subreddit.hot(limit=5):
    submission.comments.replace_more(limit=0)
    for comment in submission.comments.list():
        if comment.id not in posts_replied_to:
            if re.search(regtext, comment.body, re.IGNORECASE):
                m = re.search(regtext, comment.body, re.IGNORECASE)
                print(comment.body)
                fromcur = m.group(1).upper()
                tocur = m.group(2).upper()
                response = requests.get("https://min-api.cryptocompare.com/data/price?fsym=" + fromcur + "&tsyms=" + tocur)
                price = json.loads(response.text)
                price = str(price[tocur])
                date = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                comment.reply("Conversion Rate: 1 " + fromcur + " is worth " + price + " " + tocur +
                              "\n \n As of " + date)
                print("Bot replying to : ", comment.body)
               # posts_replied_to.append(comment.id)

with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")

