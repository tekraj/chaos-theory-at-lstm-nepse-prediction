import os
from flask import Flask, request, jsonify
from flask_cors import CORS
server = Flask(__name__)
CORS(server)

@server.route('/', methods=['GET'])
def hello():
    return '<h1>Hello</h1>'


if __name__ == "__main__":
    server.run(host='0.0.0.0', port=6060)
