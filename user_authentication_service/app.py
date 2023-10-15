#!/usr/bin/env python3
"""Route module for the API"""
from flask import Flask, jsonify


app = Flask(__name__)
app.register_blueprint()


@app.route('/', methods=['GET'], strict_slaches=False)
def welcome() -> str:
    """ Welcome route """
    return jsonify({"message": "Bienvenue"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
