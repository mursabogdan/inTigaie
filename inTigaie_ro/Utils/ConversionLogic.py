__author__ = 'bogdanmursa'


import json
from Models.Ingredient import Ingredient
from Models.Recipe import Recipe
from Utils import Constants


def toJson(object):
    return json.loads(json.dumps(object.__dict__))


def toObject(objectType, json):
    if objectType == Constants.INGREDIENT_OBJECT:
        return Ingredient(**json)
    elif objectType == Constants.RECIPE_OBJECT:
        return Recipe(**json)