# -*- coding: UTF-8 -*-
import json


def option(name):
    keys = [conf.strip() for conf in name.split('.')]
    global config
    value = config
    for _, key in enumerate(keys):
        value = value.get(key)
    return value


def get_config():
    with open('config.json', 'r') as f:
        content = json.loads(f.read())
    return content


config = get_config()
