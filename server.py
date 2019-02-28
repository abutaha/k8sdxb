#!/usr/bin/python

from flask import Flask
from flask import redirect

from pymemcache.client.base import Client as mcache
import redis
import _mysql


mc_client = mcache(('localhost', 11211))

r_client = redis.Redis(host='localhost', port=6379)

mdb = _mysql.connect(host='localhost', user='root',
                     passwd='root', db='appdb')


app = Flask(__name__)


@app.route('/')
def index():
    return 'It works!'


@app.route('/set-redis')
def setredis():
    r_client.set("mykey", "value")


@app.route('/get-redis')
def getredis():
    r_client.get("mykey")


@app.route('/set-memcache')
def setmemcache():
    mc_client.set("mykey", "value")


@app.route('/get-memcache')
def getmemcache():
    mc_client.get("mykey")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
