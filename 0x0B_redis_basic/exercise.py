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
            print("Test 1")
            return None
        if fn is None:
            print("Test 2")
            return None
        try:
            print("Test 3")
            return fn(value)
        except ValueError:
            print("Test 4")
            return value
        except Exception as a:
            print("Test 5")
            return None

    def get_str(self, key):
        """"""
        print("Test 6")
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key):
        """"""
        value = self.get(key)
        if isinstance(value, bytes):
            print("Test 7")
            return value
        print("Test 8")
        return int(value)