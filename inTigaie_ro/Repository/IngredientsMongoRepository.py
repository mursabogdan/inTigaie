__author__ = 'bogdanmursa'

from Models.Ingredient import Ingredient
from MongoRepository import MongoRepository
from Utils.ConversionLogic import toJson, toObject


class IngredientsMongoRepository(MongoRepository):

    def __init__(self, connection):
        self.list = []
        self.connection = connection

    def add(self, value):
        self.connection.insert(toJson(value))

    def update(self, value):
        pass

    def delete(self, value):
        whereClause = ""
        self.connection.remove({whereClause})

    def findOne(self, values):
        whereClause = ""
        return Ingredient(**self.connection.find_one({whereClause}, {'_id': 0}))

    def findAll(self, value):
        whereClause = ""
        for value in self.connection.find({whereClause}):
            self.list.append(toObject(value))
        return self.list

    def getAll(self):
        for value in self.connection.find():
            self.list.append(toObject(value))
        return self.list