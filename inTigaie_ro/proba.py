from Models.Ingredient import Ingredient
from Models.Recipe import Recipe
from Repository.RecipesMongoRepository import RecipesMongoRepository

__author__ = 'bogdanmursa'


repository = RecipesMongoRepository();

mazare = Ingredient("Mazare", 123, "La cutie")
cartofi = Ingredient("Cartofi", 10, "La kilogram")
patrunjel = Ingredient("Patrunjel", 1, "La legatura")
ulei = Ingredient("Ulei", 5, "La sticla")

recipe = Recipe("Salata de legume", "Se gateste foarte usor, se ia mazarea se amesteca cu cartofii fierti si se pune patrunjel dupa cu ulei", [mazare, cartofi, patrunjel, ulei])



print recipe
