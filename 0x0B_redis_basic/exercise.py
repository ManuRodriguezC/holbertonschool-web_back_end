#!/usr/bin/env python3
""" Module to connect with redis """
import redis
import uuid
from typing import Union, Callable, List
from functools import wraps


def replay(method: Callable) -> None:
    """ This function return all elements create a one key"""
    redis_db = redis.Redis()

    key_inputs = method.__qualname__ + ":inputs"
    key_outputs = method.__qualname__ + ":outputs"

    inputs: List[bytes] = redis_db.lrange(key_inputs, 0, -1)
    outputs: List[bytes] = redis_db.lrange(key_outputs, 0, -1)

    print(f"{method.__qualname__} was called {len(inputs)} time")

    for int, out in zip(inputs, outputs):
        int = int.decode()
        out = out.decode()
        print(f"{method.__qualname__}(*{int}) -> {out}")


def call_history(method: Callable) -> Callable:
    """This decorator return the values of the list"""
    def wrapper(self, *args, **kwargs):
        """"""
        keyint = method.__qualname__ + ":inputs"
        keyout = method.__qualname__ + ":outputs"
        self._redis.rpush(keyint, *args)
        outputs = method(self, *args, **kwargs)
        self._redis.rpush(keyout, outputs)
        return outputs
    return wrapper


def count_calls(method: Callable) -> Callable:
    """
    This function create key value qualname for
    count the number to called Cache class
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ When call the class, the key incremment the value 1 """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache():
    """ This class create a redis connection"""
    def __init__(self):
        """ The constructure start conection with redis. """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ This method created the set with key and value. """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: Union[str,
                             int,
                             float,
                             bytes], fn=None) -> Union[str, int, float, bytes]:
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is None:
            return value
        try:
            return fn(value)
        except ValueError:
            raise ValueError

    def get_str(self, key):
        """"""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key):
        """"""
        value = self.get(key)
        if isinstance(value, bytes):
            return value
        return int(value)
