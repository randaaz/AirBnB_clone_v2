#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Basic Flask application with a route to display a list of states.
"""
from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def appcontext_teardown(self):
    """Close the storage engine at the end of each request.
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def state_info():
    """ Display a HTML page inside the tag body"""
    return render_template('7-states_list.html',
                           states=storage.all(State))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
