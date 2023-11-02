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

    def get(self, key: Union[str, int, float, bytes], fn) -> Union[str, int, float, bytes]:
        value = self._redis.get(key)
        return value

    def get_str(self):
        """"""
        pass

    def get_int(self):
        """"""