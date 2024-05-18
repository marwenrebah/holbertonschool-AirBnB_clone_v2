#!/usr/bin/python3
"""
Write a script that starts a Flask web application:
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ” followed by the value of the text variable
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """display Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """Display HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C_is_fun(text):
    """display C followed by the value of the text variable"""
    string = "C %s" % text
    string = string.replace("_", " ")
    return string


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
