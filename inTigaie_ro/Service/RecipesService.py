from Repository.RecipesMongoRepository import RecipesMongoRepository

__author__ = 'bogdanmursa'


class RecipesService():

    def __init__(self):
        self.repository = RecipesMongoRepository()

    def getRecipesByName(self, name):
        listOfRecipes = self.repository.findAll(name)
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
        listOfClauses = []
        listOfIngredients = ingredients.split(', ')
        for ingredient in listOfIngredients:
            listOfClauses.append({'ingredients.name': ingredient})
        whereClause = ({"$and": listOfClauses})
        print whereClause
        listOfRecipes = self.repository.findAll(whereClause)
        return listOfRecipes


