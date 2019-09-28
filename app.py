import config
from flask import Flask, request, jsonify
from geopy.geocoders import Nominatim
from requests_oauthlib import OAuth1Session


twitter = OAuth1Session(
    config.CLIENT_KEY,
    client_secret=config.CLIENT_SECRET,
    resource_owner_key=config.ACCESS_KEY,
    resource_owner_secret=config.ACCESS_SECRET
)
geolocator = Nominatim(user_agent="voice_hackathon_berlin")
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


@app.route('/tweet')
def tweet_search_by_trends():
    req_body = request.args.to_dict()
    url = 'https://api.twitter.com/1.1/trends/place.json?id=638242'
    r = twitter.get(url)
    hashtags = [r.json()[0]['trends'][index]['query'] for index in range(3)]
    output = []
    for hashtag in hashtags:
        t = twitter.get("https://api.twitter.com/1.1/search/tweets.json?q={}&count=1&lang=en".format(hashtag))
        output.append({"text": t.json()['statuses'][0]['text']})
    return jsonify(status=True, location=req_body['city'], item=output)


@app.route('/tweet/coordinates')
def tweet_search_by_coordinates():
    req_body = request.args.to_dict()
    query = ','.join([req_body['lat'], req_body['lon']])
    location = str(geolocator.reverse(query))
    url = 'https://api.twitter.com/1.1/search/tweets.json'
    r = twitter.get(url + '?count=3&lang=en&geocode={}'.format(query+',1mi'))
    output = [{"text": r.json()['statuses'][index]['text']} for index in range(3)]
    return jsonify(status=True, location=location, item=output)


if __name__ == '__main__':
    app.run()
