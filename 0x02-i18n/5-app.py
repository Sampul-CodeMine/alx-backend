#!/usr/bin/env python3
"""
This is a Basic Flask App to create a simple route using Flask Babel Setup
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union, Dict


# Mock data to depict a user's logged in sessions and info
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """This is a config class for Flask Babel"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'


app = Flask(__name__)
app.config.from_object(Config)
app.debug = True
babel = Babel(app)


def get_user() -> Union[Dict, None]:
    """
    This is a function that gets the data of an assumed logged in user

    Returns:
        (dict) if the user's info as a dictionary if found else (None)
    """
    user_id = request.args.get('login_as', None)
    # print(user_id)
    if user_id is not None and int(user_id) in users.keys():
        user_details = users.get(int(user_id), None)
        # print(user_details)
        return user_details
    return None


@app.before_request
def before_request() -> None:
    """
    A function that gets executed before any function to set or get a user
    and set the user as global on `flask.g.user`
    """
    g.user = get_user()


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
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
