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
app.debug = True
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """This is a function that retrieves the locality for a webpage
    The locality or supported language will be picked from the config class

    Returns:
        str: Returns a string
    """
    lang = request.args.get('locale')
    return lang if lang in app.config['LANGUAGES'] else \
        request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """This is a basic route to the homepage

    Returns:
        str: Returns a string in the index page
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
