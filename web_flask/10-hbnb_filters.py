#!/usr/bin/python3
"""
Write a script that starts a Flask web application:
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """display states, cities and amenities"""
    states = sorted(storage.all(State).values(),
                    key=lambda item: item.name)
    amenities = sorted(storage.all(Amenity).values(),
                       key=lambda item: item.name)
    for state in states:
        state.cities = sorted(state.cities, key=lambda item: item.name)
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


@app.teardown_appcontext
def remove_sess(self):
    """removing the current SQLAlchemy Session after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
