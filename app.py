import config
from flask import Flask, request, jsonify, redirect, url_for
from requests_oauthlib import OAuth1Session

import ast
import json

twitter = OAuth1Session(
    config.CLIENT_KEY,
    client_secret=config.CLIENT_SECRET,
    resource_owner_key=config.ACCESS_KEY,
    resource_owner_secret=config.ACCESS_SECRET
)

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/news')
def news():
    return "all is great in alex"


@app.route('/test')
def test():
    url = 'https://api.twitter.com/1.1/trends/place.json?id=638242'
    r = twitter.get(url)
    return jsonify(status=True, result=r.json())


@app.route('/tweet/', methods=['POST'])
def tweet():
    body = ast.literal_eval(json.dumps(request.get_json()))
    url = 'https://api.twitter.com/1.1/trends/place.json?id=638242'
    r = twitter.get(url)
    hashtags = [r.json()[0]['trends'][index]['query'] for index in range(3)]
    output = []
    for hashtag in hashtags:
        t = twitter.get("https://api.twitter.com/1.1/search/tweets.json?q={}&count=1&lang=en".format(hashtag))
        output.append({"text": t.json()['statuses'][0]['text']})
    return jsonify(status=True, location=body['city'], item=output)


if __name__ == '__main__':
    app.run()
