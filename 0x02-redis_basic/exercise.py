#!/usr/bin/env python3
"""Radis Module"""

import redis
import uuid
from functools import wraps
from typing import Union, Optional, Callable, Any


# def count_calls(method: Callable) -> Callable:
#     """Decorator that counts how many times a method is called."""
#     @wraps(method)
#     def wrapper(self: Any, *args, **kwargs) -> str:
#         """warps called method"""
#         key = method.__qualname__
#         self._redis.incr(key)
#         return method(self, *args, **kwargs)
#     return wrapper


# def call_history(method: Callable) -> Callable:
#     """Decorator that stores input and output history of a method."""
#     @wraps(method)
#     def wrapper(self, *args):
#         """warps called method"""
#         self._redis.rpush(f'{method.__qualname__}:inputs', str(args))
#         output = method(self, *args)
#         self._redis.rpush(f'{method.__qualname__}:outputs', output)
#         return output
#     return wrapper


# def replay(fn: Callable) -> None:
#     """ Check redis for how many times a function was called and display """

#     calls = redis.Redis().get(fn.__qualname__).decode('utf-8')
#     inputs = [input.decode('utf-8') for input in
#               redis.Redis().lrange(f'{fn.__qualname__}:inputs', 0, -1)]
#     outputs = [output.decode('utf-8') for output in
#                redis.Redis().lrange(f'{fn.__qualname__}:outputs', 0, -1)]
#     print(f'{fn.__qualname__} was called {calls} times:')
#     for input, output in zip(inputs, outputs):
#         print(f'{fn.__qualname__}(*{input}) -> {output}')


class Cache:
    """Cache class"""
    def __init__(self) -> None:
        """new object"""
        self._radis = redis.Redis()
        self._radis.flushdb()

    # @call_history
    # @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store method"""
        key = str(uuid.uuid4())
        self._radis.set(key, data)
        return key

    # def get(self, key: str, fn: Optional[Callable] = None) -> Any:
    #     """get method"""
    #     data = self._radis.get(key)
    #     if not data:
    #         return
    #     if fn is int:
    #         return self.get_int(data)
    #     if fn is str:
    #         return self.get_str(data)
    #     if callable(fn):
    #         return fn(data)
    #     return data

    # def get_str(self, data: bytes) -> str:
    #     """bytes to string"""
    #     return data.decode("utf-8")

    # def get_int(self, data: bytes) -> int:
    #     """bytes to int"""
    #     return int(data)
