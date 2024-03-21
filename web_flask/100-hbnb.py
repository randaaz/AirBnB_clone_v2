#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Script to start a Flask web application for HBNB is alive.
"""

from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """Closes the current SQLAlchemy session."""
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb_page():
    """Display an HBNB HTML page."""
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda x: x.name)
    places = sorted(storage.all(Place).values(), key=lambda x: x.name)
    return render_template('100-hbnb.html', states=states,
                           amenities=amenities, places=places)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
