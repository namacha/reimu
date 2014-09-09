# -*- coding: utf-8 -*-
from sample import (
    demo1,
)


patterns = [
    (r'^!ping$', demo1.ping),
    (r'^!dice$', demo1.throw_dice),
    (r'^!parrot', demo1.parrot),
    ('hi', demo1.greet),
    ('yay', lambda msg: 'yay!'),
]
