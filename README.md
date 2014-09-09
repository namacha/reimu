reimu-core
==================
reimu-core is a core system of skypebot 'reimu'.

This system contains base system only, not including time-driven event, dynaminc message handling.


Usage
============
## Make module

`touch foo.py`

Edit foo.py

```
def ping(msg):
    '''!ping:ping-pong test'''
    return 'pong'

def greet(msg):
    name = msg.FromHandle
    return 'Hello, %s' % name
```

Function is called with argument 'msg' when chat message matches.

Function must return string/unicode.

'msg' is a instance of Skype4Py/Message.

For more information, see [Skype4Py Reference#Message](http://skype4py.sourceforge.net/doc/html/Skype4Py.chat.ChatMessage-class.html)


## Map chat text to function

Edit ./patterns.py

```
import foo
```

import user module.

```
patterns = [
    (r'^!ping$', foo.ping),
    ('hi', foo.greet),
]
```

patterns is a list defines when to call function.
patterns = [(REGEX_STRING, FUNCTION), ...]

`(r'^!help$', show_help)` is automatically added to patterns.

To generate help document, add docstring to function.

## Run bot

`python run_bot.py`


Note
================
## Timeout
Execution of all mapped function will timeout if it couldn't finish within 3 seconds.

To change timeout length, edit `PROCESS_TIMEOUT` in core/processor.py
