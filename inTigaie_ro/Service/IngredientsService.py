from Repository.IngredientsMongoRepository import IngredientsMongoRepository

__author__ = 'bogdanmursa'


class IngredientsService():

    def __init__(self):
        self.repository = IngredientsMongoRepository()

    def getIngredientsByName(self, name):
        listOfIngredients = self.repository.findAll(name)
        return listOfIngredients

    def getAllIngredients(self):
        listOfIngredients = self.repository.getAll()
        return listOfIngredients

    def orderByPrice(self, listOfIngredients):
        sortedList = sorted(listOfIngredients, key=lambda ingredient: ingredient.getPrice())
        return sortedList

    def orderByName(self, listOfIngredients):
        sortedList = sorted(listOfIngredients, key=lambda ingredient: ingredient.getName())
        return sortedList


