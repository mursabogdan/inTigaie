import Utils.ConversionLogic
__author__ = 'bogdanmursa'


class Recipe():

    def __init__(self, name, description, ingredients):
        self.ingredients = []
        self.name = name
        self.description = description
        for ingredient in ingredients:
            self.ingredients.append(Utils.ConversionLogic.toObject(Utils.ConversionLogic.Constants.INGREDIENT_OBJECT, ingredient))

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
        return self.name + "," + self.description + "," + str(self.ingredients)