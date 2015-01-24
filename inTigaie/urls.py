from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'inTigaie.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'inTigaie_ro.Controller.mainPageController.toMap', name='MainMenu'),
    url(r'^ingredients', 'inTigaie_ro.Controller.IngredientsController.toMap', name='Ingredients'),
    url(r'^recipes', 'inTigaie_ro.Controller.RecipesController.toMap',  name='Recipes'),
)
