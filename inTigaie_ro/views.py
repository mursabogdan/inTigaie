from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from Repository.IngredientsMongoRepository import IngredientsMongoRepository


def Ingredients(request):
    repository = IngredientsMongoRepository()
    ingredient_list = repository.getAll()
    c = RequestContext(request, {'ingredient_list': ingredient_list})
    return render_to_response('ingredients.html', c)