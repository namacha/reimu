# -*- coding: utf-8 -*-
from sample import (
    demo1,
    SimpleTimer,
)


timer = SimpleTimer.Timer()

patterns = [
    (r'^!ping$', demo1.ping),
    (r'^!dice$', demo1.throw_dice),
    (r'^!parrot', demo1.parrot),
    ('hi', demo1.greet),
    ('yay', lambda msg: 'yay!'),
    (r'!timer \d+\s?.*', timer.set_timer)
]


schedules = [
    timer.has_arrived,
]
