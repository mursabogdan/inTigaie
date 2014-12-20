__author__ = 'bogdanmursa'

from Models.Ingredient import Ingredient
from MongoRepository import MongoRepository
from Utils.ConversionLogic import toJson

class IngredientsMongoRepository(MongoRepository):

    def __init__(self, connection):
        self.list = []
        self.connection = connection

    def add(self, value):
        self.connection.insert(toJson(value))

    def update(self, value):
        pass

    def delete(self, value):
        self.list.pop(value)

    def findOne(self, values):
        return Ingredient(**self.connection.find_one({}, {'_id': 0}))

    def findAll(self, value):
        for value in self.connection.find():
            self.list.append(Ingredient(**value))
        return self.list

    def getAll(self):
        for value in self.connection.find():
            self.list.append(Ingredient(**value))
        return self.list