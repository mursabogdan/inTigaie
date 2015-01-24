__author__ = 'bogdanmursa'


class Ingredient():

    def __init__(self, name=" ", price=" ", description=" "):
        self.name = name
        self.price = price
        self.description = description

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def getDescription(self):
        return self.description

    def setName(self, name):
        self.name = name

    def setPrice(self, price):
        self.price = price

    def setDescription(self, description):
        self.description = description

    def toString(self):
        return self.name + "," + str(self.price) + "," + self.description
