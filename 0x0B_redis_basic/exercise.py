#!/usr/bin/env python3
""" Module to connect with redis """
import redis
import uuid
from typing import Union, Callable as fn


class Cache():
    """ This class create a redis connection"""
    def __init__(self):
        """ The constructure start conection with redis. """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        This method created the set with key and value.
        Parameters
        ----------
        data: String
            If the value of the key to save in redis db.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: Union[str, int, float, bytes], fn=None) -> Union[str, int, float, bytes]:
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is None:
            return value
        try:
            return fn(value)
        except ValueError:
            return "ValueError"


    def get_str(self, key):
        """"""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key):
        """"""
        value = self.get(key)
        if isinstance(value, bytes):
            return value
        return int(value)