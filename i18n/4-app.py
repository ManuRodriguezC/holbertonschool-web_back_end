#!/usr/bin/env python3
""" This module create a flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _
from typing import Union


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

def get_locale():
    """ This function accept the best lenguages of the web"""
    LENGUAGE: Union[str, None] = request.args.get("locale", None)

    if LENGUAGE is not None and LENGUAGE in app.config["LANGUAGES"]:
        return LENGUAGE

    return request.accept_languages.best_match(
        app.config["LANGUAGES"]
    )


@app.route("/")
def index():
    """ This funtion return the index web """
    return render_template("4-index.html"), 200


if __name__ == "__main__":
    app.run()
