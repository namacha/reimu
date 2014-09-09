# -*- coding: utf-8 -*-
import re


def is_match(regexp):
    def _is_match(msg):
        if regexp.search(msg.Body) is not None:
            return True
        else:
            return False
    return _is_match


def makeconditions(args):
    ls = [(is_match(re.compile(pattern)), action) for pattern, action in args]
    return ls
