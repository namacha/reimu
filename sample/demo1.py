# -*- coding: utf-8 -*-
from random import randint 


def ping(msg):
    '''ping!'''
    return 'pong'


def greet(msg):
    '''bot greets you'''
    name = msg.FromDisplayName
    return 'Hello, %s' % name


def throw_dice(msg):
    result = randint(1, 7)
    return '%d' % result


def parrot(msg):
    text = msg.Body
    return text
