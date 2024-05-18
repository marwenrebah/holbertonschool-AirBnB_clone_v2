#!/usr/bin/python3
"""
Write a script that starts a Flask web application:
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def list_of_states():
    """display a list of all State objects
    present in DBStorage sorted by name"""

    stateslist = {}
    for state in storage.all(State).values():
        stateslist[state.id] = state.name
    stateslist = dict(sorted(stateslist.items(), key=lambda item: item[1]))
    return render_template("7-states_list.html", statesdict=stateslist.items())


@app.teardown_appcontext
def remove_sess(self):
    """removing the current SQLAlchemy Session after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
