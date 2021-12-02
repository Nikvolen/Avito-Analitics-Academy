import doctest
from morse import encode


def test_morse(string):
    """
    >>> test_morse('SOS')
    '... --- ...'
    >>> test_morse('OOOOOOOOO') # doctest: +ELLIPSIS
    '--- ... ---'
    >>> encode('S O      S') # doctest: +NORMALIZE_WHITESPACE
    '... --- ...'
    >>> test_morse('sos')
    Traceback (most recent call last):
    KeyError: 's'
    >>> test_morse(1337)
    Traceback (most recent call last):
    TypeError: 'int' object is not iterable
    """

    return encode(string)


if __name__ == '__main__':
    doctest.testmod()
