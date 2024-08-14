#!/usr/bin/env python3
"""Radis Module"""

import redis
import uuid
from typing import Union, Optional, Callable, Any


class Cache:
    """Cache class"""
    def __init__(self):
        """new object"""
        self._radis = redis.Redis()
        self._radis.flushdb()

    def store(self, data: Union[str, int, bytes, float]) -> str:
        """store method"""
        key = str(uuid.uuid4())
        self._radis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """get method"""
        data = self._radis.get(key)
        if not data:
            return
        if fn is int:
            return self.get_int(data)
        if fn is str:
            return self.get_str(data)
        if callable(fn):
            return fn(data)
        return data

    def get_str(self, data: bytes) -> str:
        """bytes to string"""
        return data.decode("utf-8")

    def get_int(self, data: bytes) -> int:
        """bytes to int"""
        return int(data)
