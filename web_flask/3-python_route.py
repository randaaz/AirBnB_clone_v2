#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Basic Flask application with routes for root,
'/hbnb', '/c/<text>', and '/python/<text>'.
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
def c_text(text=None):
    """Args:
        text (str): The text to be displayed.

    Returns:
        str: Formatted string with 'C ' followed by the text."""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python_text(text='is_cool'):
    """Args:
        text (str): The text to be displayed.

    Returns:
        str: Formatted string with 'Python ' followed by the text."""
    return "Python {}".format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
