#!/usr/bin/env python3
"""Route module for the API"""
import flask
from typing import Tuple


app = flask.Flask(__name__)
app.register_blueprint()


@app.route('/', methods=['GET'], strict_slaches=False)
def welcome() -> Tuple[flask.Response, int]:
    """ Welcome route """
    return flask.jsonify({"message": "Bienvenue"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
