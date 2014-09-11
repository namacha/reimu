# -*- coding: utf-8 -*-
import time


class Timer(object):

    def __init__(self):
        self.timers = []

    def set_timer(self, msg):
        args = msg.split(' ')
        limit = int(args[1]) + time.time()
        if len(args) > 2:
            limit_message = args[2]
        else:
            limit_message = "It's time!"
        self.timers.append((limit, limit_message, msg))
        return 'OK'

    def has_arrived(self):
        now = time.time()
        for ls in self.timers:
            limit, limit_message, msg = ls
            if now > limit:
                self.timers.remove(ls)
                return msg, limit_message
        return False
