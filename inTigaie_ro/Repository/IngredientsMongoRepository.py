__author__ = 'bogdanmursa'

from Models.Ingredient import Ingredient
from MongoRepository import MongoRepository
from Utils.ConversionLogic import toJson, toObject
from Utils import Constants
from Utils.MongoConnectionManager import MongoConnectionManager



class IngredientsMongoRepository(MongoRepository):

    def __init__(self):
        self.list = []

    def add(self, value):
        try:
            connection = MongoConnectionManager(Constants.DB, Constants.INGREDIENT_COLLECTION)
            connection.insert(toJson(value))
        except Exception:
            pass

    def update(self, value):
        pass

    def delete(self, value):
        whereClause = {}
        self.connection.remove({whereClause})

    def findOne(self, whereClause):
        try:
            mongoClient = MongoConnectionManager(Constants.DB, Constants.INGREDIENT_COLLECTION)
            return toObject(Constants.INGREDIENT_OBJECT, mongoClient.connection.find_one(whereClause, {'_id': 0}))
        except Exception:
            return []

    def findAll(self, whereClause):
        try:
            mongoClient = MongoConnectionManager(Constants.DB, Constants.INGREDIENT_COLLECTION)
            for value in mongoClient.connection.find(whereClause, {'_id': 0}):
                self.list.append(toObject(Constants.INGREDIENT_OBJECT, value))
            return self.list
            mongoClient.closeConnection()
        except Exception:
            return []

    def getAll(self):
        for value in self.connection.find():
            self.list.append(toObject(value))
        return self.list