from django.shortcuts import render
from .models import Recipe
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.
class RecipeListView(ListView):
    model = Recipe
    template_name = 'list.html'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'