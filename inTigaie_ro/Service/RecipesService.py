from Repository.RecipesMongoRepository import RecipesMongoRepository
from Utils import Constants

__author__ = 'bogdanmursa'


class RecipesService():

    def __init__(self):
        self.repository = RecipesMongoRepository()

    def getRecipesByName(self, names):
        listOfNames = names.split(',')
        listOfRecipes = self.repository.findAll(listOfNames, Constants.SEARCH_BY_NAME)
        return listOfRecipes

    def getAllRecipes(self):
        listOfRecipes = self.repository.getAll()
        return listOfRecipes

    def orderByPrice(self, listOfRecipes):
        sortedList = sorted(listOfRecipes, key=lambda recipe: recipe.getPrice())
        return sortedList

    def orderByName(self, listOfRecipes):
        sortedList = sorted(listOfRecipes, key=lambda recipe: recipe.getName())
        return sortedList

    def getRecipeByIngredients(self, ingredients):
        listOfIngredients = ingredients.split(',')
        listOfRecipes = self.repository.findAll(listOfIngredients, Constants.SEARCH_BY_INGREDIENTS)
        return listOfRecipes


