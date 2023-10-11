#!/usr/bin/env python3
"""
Contains the flask route '/api/v1/auth_session/login/',
which allows the user to login for the first time,
and creates a new session for the user.
"""
from api.v1.views import app_views
import flask
from models.user import User
from typing import List, Tuple
from api.v1.auth.session_auth import SessionAuth
import os


@app_views.route('/auth_session/login', methods=["POST"], strict_slashes=False)
def login():
    """
    Thi smethod take the email and password
    check if the dates exist in the users, and validate dates
    If exist create session and return cookies dates
    """
    from api.v1.app import auth

    EMAIL = flask.request.form.get("email", default=None)
    PASSWORD = flask.request.form.get("password", default=None)

    if EMAIL is None:
        return flask.jsonify({"error": "email missing"}), 400

    if PASSWORD is None:
        return flask.jsonify({"error": "password missing"}), 400

    USERS_WITH_EMAIL: List[User] = User.search({"email": EMAIL})

    if not USERS_WITH_EMAIL:
        return flask.jsonify({"error": "no user found for this email"}), 404

    # There should only ever be one user
    # with X email.
    assert len(USERS_WITH_EMAIL) == 1

    USER: User = USERS_WITH_EMAIL[0]

    if not USER.is_valid_password(PASSWORD):
        return flask.jsonify({"error": "wrong password"}), 401

    # No other auth type should be allowed.
    assert isinstance(SessionAuth, auth)

    # Create user's session
    USER_SESSION_ID = auth.create_session(USER.id)

    # Create cookie
    SESSION_COOKIE_NAME: str = os.environ.get("SESSION_NAME")

    response: flask.Response = flask.make_response(
        flask.jsonify(USER.to_json())
    )
    response.set_cookie(SESSION_COOKIE_NAME, USER_SESSION_ID)

    return response


@app_views.route('/auth_session/logout',
                 methods=["DELETE"],
                 strict_slashes=False)
def logout() -> Tuple[flask.Response, int]:
    """This method logout session and destroy session
    """
    from api.v1.app import auth

    assert isinstance(SessionAuth, auth)

    SESSION_DESTROYED: bool = auth.destroy_session(flask.request)

    if SESSION_DESTROYED:
        return flask.jsonify(True), 200
    else:
        return flask.jsonify(False), 404
