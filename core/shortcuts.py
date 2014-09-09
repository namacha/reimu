# -*- coding: utf-8 -*-
from functools import wraps


def response_only(name):
    def _decorator(func):
        @wraps(func)
        def _wrapper(msg):
            sender = msg.FromHandle
            if sender == name:
                return func(msg)
            else:
                return ''
        return _wrapper
    return _decorator


def emphasize(func):
    @wraps(func)
    def _decorator(msg):
        result = func(msg)
        return '/me ' + result
    return _decorator
