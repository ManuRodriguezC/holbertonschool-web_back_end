#!/usr/bin/env python3
""" This module create a flask app"""
from flask import Flask, render_template
from flask_babel import Babel


class Config():
    LANGUAGES = ["en" , "fr"]
    BABEL_DEFAULT_LOCATE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
bable = Babel(app, Config.BABEL_DEFAULT_LOCATE, Config.BABEL_DEFAULT_TIMEZONE)



@app.route("/")
def index():
    """ This funtion return the index web """
    return render_template("0-index.html"), 200


if __name__ == "__main__":
    app.run()
