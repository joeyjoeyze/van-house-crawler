# -*- coding: UTF-8 -*-
import sys
from type_converter import auto_convert


def parse_argv():
    """
    parse system arguments

    :return: Dict
    """

    # init options dict
    options = {}

    # loop through arguments
    for argument in sys.argv[1:]:
        # if option found
        if argument[:2] == '--':
            # get separator position
            separator = argument.find('=')

            # if is flag usage
            if separator == -1:
                options[argument[2:]] = True

            # if is params usage
            else:
                options[argument[2:separator]] = auto_convert(argument[separator + 1:])

    return options
