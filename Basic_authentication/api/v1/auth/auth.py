from flask import request
from typing import List, TypeVar


class Auth():
    """"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """"""
        if path is None or excluded_paths is None:
            return True
        return path not in excluded_paths and path + "/" not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """"""
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        else:
            return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """"""
        return None
