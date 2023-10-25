#!/usr/bin/env python3
""" This module create a flask app"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
bable = Babel(app)
app.config["en", "fr"]

class Config():
    LANGUAGES = ["en" , "fr"]


@app.route("/")
def index():
    """ This funtion return the index web """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run()
