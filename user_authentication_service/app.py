#!/usr/bin/env python3
"""Route module for the API"""
from flask import Flask, jsonify, Response, request, abort, make_response
from typing import Tuple, Optional
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome() -> Tuple[Response, int]:
    """ Welcome route """
    return jsonify({"message": "Bienvenue"}), 200


@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> Tuple[Response, int]:
    """"""
    EMAIL: Optional[str] = request.form.get("email")
    PASSWORD: Optional[str] = request.form.get("password")

    try:
        AUTH.register_user(EMAIL, PASSWORD)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
    else:
        return jsonify({"email": "<registered email>",
                        "message": "user created"}), 200


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> Tuple[Response, int]:
    """"""
    EMAIL: Optional[str] = request.form.get("email")
    PASSWORD: Optional[str] = request.form.get("password")

    if not AUTH.valid_login(EMAIL, PASSWORD):
        abort(401)

    SESSION_ID = AUTH.create_session(EMAIL)

    if SESSION_ID is None:
        abort(401)

    response: Response = make_response(jsonify({"email": EMAIL,
                                                "message": "logged in"}))
    response.set_cookie("session_id", SESSION_ID)
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
