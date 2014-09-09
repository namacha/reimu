reimu-core
==================
reimu-core is a core system of skypebot 'reimu'.

This system contains base system only, not including time-driven event, dynaminc message handling.


Usage
============
## Make module

`touch foo.py`

edit foo.py

```
def ping(msg):
    return 'pong'

def greet(msg):
    name = msg.FromHandle
    return 'Hello, %s' % name
```

function is called when chat message matches with argument 'msg'.

## Edit core/mapping.py

```
import foo
```

import user defined function.

```
patterns = [
    (r'^!ping$', ping),
    ('hi', greet),
]
```

patterns is a list defines when to call function.
patterns = [(REGEX_STRING, FUNCTION), ...]


## Run bot

`python run_bot.py`
