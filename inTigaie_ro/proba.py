from Models.Ingredient import Ingredient
from Repository.RecipesMongoRepository import RecipesMongoRepository

__author__ = 'bogdanmursa'


repository = RecipesMongoRepository();

mazare = Ingredient("Mazare", 123, "La cutie")
cartofi = Ingredient("Cartofi", 10, "La kilogram")
patrunjel = Ingredient("Patrunjel", 1, "La legatura")
ulei = Ingredient("Ulei", 5, "La sticla")


listOfObjects = [mazare, cartofi, patrunjel, ulei]


result = repository.findOne({'ingredients.name': 'Piper'})

print result.toString()