# -*- coding: UTF-8 -*-


def boolify(string):
    """
    convert string to boolean type

    :param string: string
    :return: bool
    """

    if string == 'True' or string == 'true':
        return True
    if string == 'False' or string == 'false':
        return False
    raise ValueError("wrong type")


def auto_convert(string):
    """
    convert string to corresponding type

    :param string: string
    :return: bool|int|float|string
    """

    for fn in (boolify, int, float):
        try:
            return fn(string)
        except ValueError:
            pass
    return string
