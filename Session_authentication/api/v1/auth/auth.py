#!/usr/bin/env python3
"""Module Auth"""
from flask import request
from typing import List, TypeVar


class Auth():
    """Class auth and create the methos necesary of teh autheticate"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """This method check if the path is in the list"""
        if path is None or excluded_paths is None:
            return True
        return path not in excluded_paths and path + "/" not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """ This method check if is authorizate"""
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        else:
            return request.headers['Authorization']
