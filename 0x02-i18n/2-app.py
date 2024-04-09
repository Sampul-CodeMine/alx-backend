#!/usr/bin/env python3
"""
This is a Basic Flask App to create a simple route using Flask Babel Setup
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """This is a config class for Flask Babel"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'


app = Flask(__name__)
app.config.from_object(Config)
app.debug = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """This is a function that retrieves the locality for a webpage

    Returns:
        str: Returns a string
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """This is a basic route to the homepage

    Returns:
        str: Returns a string in the index page
    """
    return render_template('2-index.html', title='Welcome to Holberton')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
