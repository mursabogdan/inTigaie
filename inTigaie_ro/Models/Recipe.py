__author__ = 'bogdanmursa'


class Recipe():

    def __init__(self, name, description, ingredients):
        self.name = name
        self.description = description
        self.ingredients = ingredients

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getIngredients(self):
        return self.ingredients

    def setName(self, name):
        self.name = name

    def setDescription(self, description):
        self.description = description

    def setIngredients(self, ingredients):
        self.ingredients = ingredients

    def toString(self):
        return self.name + "," + self.description + "," + self.ingredients