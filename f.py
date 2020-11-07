#!/usr/bin/env python

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def test():
    return request.cookies['__Secure-Name']

if __name__ == "__main__":
    app.run(ssl_context=('./ssl.cert','./ssl.key'))
