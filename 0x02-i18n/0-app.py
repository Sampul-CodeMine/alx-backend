#!/usr/bin/env python3
"""
This is a Basic Flask App to create a simple route
"""
from flask import Flask, render_template


app = Flask(__name__)
app.debug = False


@app.route('/', strict_slashes=False)
def index() -> str:
    """This is a basic route to the homepage

    Returns:
        str: Returns a string in the index page
    """
    return render_template('0-index.html', title='Welcome to Holberton')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
