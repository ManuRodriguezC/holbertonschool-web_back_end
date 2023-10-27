#!/usr/bin/env python3
""" This module create a flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _
from typing import Union
import flask


class Config():
    """ This class contein the configurate of the bable flask"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(
    app,
    Config.BABEL_DEFAULT_LOCALE,
    Config.BABEL_DEFAULT_TIMEZONE
)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale():
    """ This function accept the best lenguages of the web"""
    LENGUAGE: Union[str, None] = request.args.get("locale", None)

    if LENGUAGE is not None and LENGUAGE in app.config["LANGUAGES"]:
        return LENGUAGE

    return request.accept_languages.best_match(
        app.config["LANGUAGES"]
    )


def get_user() -> Union[dict, None]:
    """
    Return a user id, id the login_as exist in to users
    """
    ID: Union[str, None] = request.args.get("login_as")

    try:
        ID_INT = int(ID)
    except Exception:
        return None

    return users.get(ID_INT)


@app.before_request
def before_request():
    """ If user exist, return you datas """
    USER: Union[dict, None] = get_user()
    flask.g.user = USER


@app.route("/")
def index():
    """ This funtion return the index web """
    return render_template("5-index.html"), 200


if __name__ == "__main__":
    app.run()
