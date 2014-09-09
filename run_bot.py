from core import (
    processor,
    mapping,
)

from patterns import patterns



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

if __name__ == '__main__':
    while True:
        try:
            conditions = mapping.makeconditions(patterns)

            p = processor.Processor(conditions)
            p.run()

            # reload all modules
            reload(processor)
            reload(mapping)
            reload(patterns)
            for module in dir(mapping):
                _module = mapping.__dict__[module]
                if '__file__' in dir(_module):
                    print 'reloading %s' % _module.__name__
                    reload(_module)
        except KeyboardInterrupt:
            exit(0)
