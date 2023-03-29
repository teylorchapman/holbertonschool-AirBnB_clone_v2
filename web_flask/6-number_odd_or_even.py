#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def howdy_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb', methods=['GET'], strict_slashes=False)
def heckinhbnb():
    return "HBNB"


@app.route('/c/<text>', methods=['GET'], strict_slashes=False)
def c_sux(text):
    return "C {}".format(text.replace("_", " "))


@app.route('/python', methods=['GET'], strict_slashes=False)
@app.route('/python/<text>', methods=['GET'], strict_slashes=False)
def python_goat(text='is cool'):
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', methods=['GET'], strict_slashes=False)
def numero_routero(n):
    return "{} is a number".format(n)

09
@app.route('/number_template/<int:n>', methods=['GET'], strict_slashes=False)
def numero_tempero(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def numba_odd_even(n):
    """ Displays an HTML page only if n is an integer """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
