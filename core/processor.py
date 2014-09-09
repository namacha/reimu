# -*- coding: utf-8 -*-

import signal
import functools
import Queue
import traceback

import Skype4Py

from status import (
    BOT_EXIT,
    BOT_RESTART
)


PROCESS_TIMEOUT = 3

TimeOutException = type("TimeOutException", (Exception, ), {})


class Processor(object):

    def __init__(self, conditions):
        self.skype = Skype4Py.Skype(Transport='x11')
        self.skype.Attach()
        self.skype.OnMessageStatus = self.receive_handler
        self.conditions = conditions
        self.queue = Queue.Queue()

        self.ignores = []

    def receive_handler(self, msg, event):
        received = Skype4Py.enums.cmsReceived
        if event == received:

            msg.MarkAsSeen()

            if msg.Body == '!ignoreme':
                if msg.FromHandle not in self.ignores:
                    self.ignores.append(msg.FromHandle)
            elif msg.Body == '!imlonely':
                if msg.FromHandle in self.ignores:
                    self.ignores.remove(msg.FromHandle)

            for condition, action in self.conditions:
                if condition(msg) is True:
                    if msg.FromHandle not in self.ignores:
                        self.queue.put((msg, action))
                        break

    def run(self):
        while True:
            try:
                msg, action = self.queue.get(True, 10)  # 10sec
                action_with_timeout =\
                    self.set_timeout(PROCESS_TIMEOUT)(action)
                result = action_with_timeout(msg)

                if result == BOT_EXIT:
                    msg.Chat.SendMessage('bye..')
                    exit()

                if result == BOT_RESTART:
                    signal.alarm(0)
                    break

                if isinstance(result, basestring):
                    if len(result) > 0:
                        msg.Chat.SendMessage(result)

            except Queue.Empty:
                # Write time-driven event here
                pass

            except TimeOutException:
                msg.Chat.SendMessage(u'ゆ…ゆっ……')
                print 'Timed out: %s' % (msg.Body)

            except Exception:
                msg.Chat.SendMessage(u'ゆ……ゆ……ゆっぐ……')
                error_message = traceback.format_exc()
                print error_message

    @staticmethod
    def set_timeout(limit):
        def alert(signum, frame):
            raise TimeOutException

        def _decorator(function):
            @functools.wraps(function)
            def _wrapper(*args, **kwargs):
                signal.signal(signal.SIGALRM, alert)
                signal.alarm(limit)
                result = function(*args, **kwargs)
                signal.alarm(0)
                return result
            return _wrapper
        return _decorator
