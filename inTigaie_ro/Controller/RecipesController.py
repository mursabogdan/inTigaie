from django.shortcuts import render_to_response
from django.template import RequestContext
from Service.RecipesService import RecipesService

__author__ = 'bogdanmursa'


def toMap(request):
    recipesService = RecipesService();
    message = 'Your Result'

    if request.GET.get('ingredients'):
        ingredients = request.GET.get('ingredients')
        recipesList = recipesService.getRecipeByIngredients(ingredients)
        c = RequestContext(request, {'recipesList': recipesList, 'response':message})
        return render_to_response('recipes.html', c)
    if request.GET.get('name'):
        name = request.GET.get('name')
        recipesList = recipesService.getRecipesByName(name)
        c = RequestContext(request, {'recipesList': recipesList, 'response':message})
        return render_to_response('recipes.html', c)
    recipesList = recipesService.getAllRecipes()

    c = RequestContext(request, {'recipesList': recipesList})
    return render_to_response('recipes.html', c)

