#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Basic Flask application with routes
for root, '/hbnb', and '/c/<text>'.
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Returns:
        str: 'Hello HBNB!'"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns:
        str: 'HBNB'"""
    return 'HBNB'


@app.route('/c/<string:text>', strict_slashes=False)
def text(text=None):
    """Args:
        text (str): The text to be displayed.

    Returns:
        str: Formatted string with 'C ' followed by the text."""
    return "C {}".format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
