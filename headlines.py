# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template
import feedparser

app = Flask(__name__)
RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn': 'http://rss.cnn.com/rss/edition.rss',
             'reuters': 'http://feeds.reuters.com/reuters/worldNews'
            }

@app.route("/")
@app.route("/<publication>")
def get_news(publication="bbc"):
    feed = feedparser.parse(RSS_FEEDS[publication])
    return render_template("home.html", articles=feed['entries'])

if __name__ == '__main__':
    app.run(port=5000, debug=True)