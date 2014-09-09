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


patterns = [
]



def make_help(msg):
    u'''!help:ヘルプもどきを表示'''
    result = u'       <この中は省略不可> (省略可)\n'
    result += u'全てのコマンドは2秒以上でタイムアウトします。\n'
    result += u'!ignoreme: れいむに無視されます\n'
    result += u'!imlonely: やっぱり構って\n'
    for pattern, func in patterns:
        func_name = func.__name__
        if func_name != '_handler':
            if func.__doc__ is not None:
                doc = func.__doc__.replace(':', ':' + ' ' * 5)
                result += '%s\n' % doc

    return result


patterns.append((r'^!help$', make_help))

conditions = makeconditions(patterns)
