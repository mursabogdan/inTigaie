__author__ = 'bogdanmursa'

from MongoRepository import MongoRepository
from Utils.ConversionLogic import toJson, toObject
from Utils import Constants
from Utils.MongoConnectionManager import MongoConnectionManager


class RecipesMongoRepository(MongoRepository):

    def __init__(self):
        self.list = []

    def add(self, value):
        try:
            mongoClient = MongoConnectionManager(Constants.DB, Constants.INGREDIENT_COLLECTION)
            mongoClient.connection.insert(toJson(value))
            return True
        except Exception:
            return False

    def update(self, value):
        pass

    def delete(self, whereClause):
        try:
            mongoClient = MongoConnectionManager(Constants.DB, Constants.RECIPES_COLLECTION)
            mongoClient.connection.remove(whereClause)
            return True
        except Exception:
            return False

    def findOne(self, whereClause):
        try:
            mongoClient = MongoConnectionManager(Constants.DB, Constants.RECIPES_COLLECTION)
            return toObject(Constants.RECIPE_OBJECT, mongoClient.connection.find_one(whereClause, {'_id': 0}))
            mongoClient.closeConnection()
        except Exception:
            return []

    def findAll(self, whereClause):
        try:
            mongoClient = MongoConnectionManager(Constants.DB, Constants.RECIPES_COLLECTION)
            for value in mongoClient.connection.find(whereClause, {'_id': 0}):
                self.list.append(toObject(Constants.RECIPE_OBJECT, value))
            return self.list
            mongoClient.closeConnection()
        except Exception:
            return []

    def getAll(self):
        try:
            mongoClient = MongoConnectionManager(Constants.DB, Constants.RECIPES_COLLECTION)
            for value in mongoClient.connection.find({}, {'_id': 0}):
                self.list.append(toObject(Constants.RECIPE_OBJECT, value))
            return self.list
            mongoClient.closeConnection()
        except Exception:
            return []