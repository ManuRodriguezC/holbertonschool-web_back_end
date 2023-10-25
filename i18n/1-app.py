#!/usr/bin/env python3
""" This module create a flask app"""
from flask import Flask, render_template
from flask_babel import Babel


class Config():
    """ This class contein the configurate of the bable flask"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app, Config.BABEL_DEFAULT_LOCALE, Config.BABEL_DEFAULT_TIMEZONE)


@app.route("/")
def index():
    """ This funtion return the index web """
    return render_template("0-index.html"), 200


if __name__ == "__main__":
    app.run()
