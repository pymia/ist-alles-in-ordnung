import config
from flask import Flask, jsonify
from requests_oauthlib import OAuth1Session

twitter = OAuth1Session('ko18rwNOfM2yADdnKnjtjmi63',
                        client_secret='nPChoV23IJpQjJDDqVFg64ht5RNMSZ1dfm0ZQdZsfoTfZt8Jyd',
                        resource_owner_key='977907642-fIu0F5gnwxL9H7gm5ambXHaDbMHhwjLS5HiSEi14',
                        resource_owner_secret='9OJpJKujDWqcXVdPVy6fesgo6Gj6Hw3ttyJb8h1FtEtOV')

url = 'https://api.twitter.com/1.1/trends/place.json?id=638242'
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
    trends_url = [r.json()['trends'][index]['url'] for index in range(3)]
    return jsonify(status=True, result=trends_url)

if __name__ == '__main__':
    app.run()
