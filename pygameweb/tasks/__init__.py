"""Basic queue for doing jobs. And such.

https://pypi.python.org/pypi/pq
"""

from pygameweb.config import Config
from pq import PQ

def put(name, what, when=None):
    """ Put something on a queue

    Example:
        >>> put('apples', {'yeahs!':1})
        >>> put('apples', {'yeahs!':2}, when='5m')

        >>> get('apples')
        {'yeahs!':2}

        Then there is nothing for a while.
        >>> get('apples')

        After five minutes passes we have something again.
        >>> get('apples')
        {'yeahs!':1}
    """
    return queue(name)[name].put(what, when)


def get(name):
    """ data for the named queue.
    """
    return queue(name)[name]


def queue(name, session=None, engine=None):
    """ gives use a queue back for working with.

    :Example:
        >>> queue('apples').put({})

    """
    if engine is None:
        engine = session.get_bind()

    connection = engine.raw_connection()
    return PQ(connection.connection)
