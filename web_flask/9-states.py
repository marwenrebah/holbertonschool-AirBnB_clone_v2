#!/usr/bin/python3
"""
Write a script that starts a Flask web application:
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states", defaults={"id": None}, strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def list_of_states(id):
    """display a list of all states"""
    states = sorted(storage.all(State).values(),
                    key=lambda item: item.name)
    for state in states:
        state.cities = sorted(state.cities, key=lambda item: item.name)
    stateid = None
    allstates = None
    if id is not None:
        stateid = "State." + str(id)
        allstates = storage.all(State)
    return render_template("9-states.html", states=states, id=id,
                           stateid=stateid, allstates=allstates)


@app.teardown_appcontext
def remove_sess(self):
    """removing the current SQLAlchemy Session after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
