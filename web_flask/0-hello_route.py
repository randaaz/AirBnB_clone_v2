#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Simple flask app that returns "Hello HBNB!" on the root route
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Returns:
        str: 'Hello HBNB!"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
