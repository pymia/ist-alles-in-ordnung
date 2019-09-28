import config
from flask import Flask, jsonify
from requests_oauthlib import OAuth1Session

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


if __name__ == '__main__':
    app.run()
