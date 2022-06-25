import random

import requests
from flask import Flask, request
import requests

lb = Flask(__name__)

MANGO_BACKENDS = ['localhost:8081', 'localhost:8082']
APPLE_BACKENDS = ['localhost:9081', 'localhost:9082']


@lb.route('/mango')
def handle_path_mango():
    response = requests.get(f"http://{random.choice(MANGO_BACKENDS)}")
    return response.content, response.status_code


@lb.route('/apple')
def handle_path_apple():
    response = requests.get(f"http://{random.choice(APPLE_BACKENDS)}")
    return response.content, response.status_code


@lb.route('/')
def hello_world():  # put application's code here
    host_header = request.headers['HOST']
    if host_header == "www.mango.com":
        response = requests.get(f"http://{random.choice(MANGO_BACKENDS)}")
        return response.content, response.status_code
    elif host_header == "www.apple.com":
        response = requests.get(f"http://{random.choice(APPLE_BACKENDS)}")
        return response.content, response.status_code
    else:
        return 'not found', 404


if __name__ == '__main__':
    lb.run()
