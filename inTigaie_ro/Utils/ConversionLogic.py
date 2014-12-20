__author__ = 'bogdanmursa'


import json


def toJson(object):
    return json.dumps(object.__dict__)