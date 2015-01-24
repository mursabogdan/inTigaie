from django.shortcuts import render_to_response
from django.template import RequestContext
from Service.IngredientsService import IngredientsService


def toMap(request):
    ingredientsService = IngredientsService()
    message = 'Your Result'
    if request.GET.get('name') != '':
        name = request.GET.get('name')
        whereClause = {'name': name}
        listOfIngredients = ingredientsService.getIngredientsByName(whereClause)
        c = RequestContext(request, {'ingredientList': listOfIngredients, 'response':message})
        return render_to_response('ingredients.html', c)
    listOfIngredients = ingredientsService.getAllIngredients()

    c = RequestContext(request, {'ingredientList': listOfIngredients})
    return render_to_response('ingredients.html', c)

