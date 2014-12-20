from Utils import Constants
from Utils.MongoConnectionManager import MongoConnectionManager

__author__ = 'bogdanmursa'

from pymongo import Connection
from Models.Ingredient import Ingredient
import json
from Repository.IngredientsMongoRepository import IngredientsMongoRepository

ingredient = Ingredient("Cartofi","10","Cei mai smecheri")

repository = IngredientsMongoRepository()
#repository.add(ingredient)
#repository.delete({'name':'Cartofi'})
values = repository.getAll()
# print values.toString()
for value in values:
    print value.toString()

#
# database_name = 'test'
# collection = 'ingredients'
# connection = Connection()
#
# collection = Connection()[database_name][collection]
# ########################################################################
# ingredient = Ingredient("Piper","123","E iute")
# #######################################################################
# def toJson(object):
#     return json.dumps(object.__dict__)
#
# ingredient_to_json = toJson(ingredient)
# ########################################################################
#
#
# whereClause = {'name':'Piper'}
#
# def toObject(objectType, json):
#     if objectType == "Ingredient":
#         return Ingredient(**json)
#     elif objectType == "Recipe":
#         return json
#
#
# print toObject('Ingredient', collection.find_one(whereClause, {'_id': 0})).toString()
#
#
#
#
# #collection.insert({"name":"Adelina"})
# list = []
#
# #for e in collection.find({}, {'_id':0}):
#  #   list.append(toObject("Ingredient", e))
#
# #for i in list:
#  #   print i.toString()
