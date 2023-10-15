#!/usr/bin/env python3
"""Route module for the API"""
from flask import Flask, jsonify, Response, request, abort
from flask import make_response, redirect, url_for
from typing import Tuple, Optional
from sqlalchemy.orm.exc import NoResultFound
from auth import Auth
from user import User


AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def bienvenue() -> Tuple[Response, int]:
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


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """This route Delete the session ID"""
    SESSION_ID: Optional[str] = request.cookies.get("session_id")

    if SESSION_ID is None:
        abort(403)

    USER: Optional[User] = Auth.get_user_from_session_id(SESSION_ID)

    if USER is None:
        abort(403)

    try:
        Auth.destroy_session(SESSION_ID)
    except NoResultFound:
        abort(403)
    return redirect(url_for('bienvenue'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
