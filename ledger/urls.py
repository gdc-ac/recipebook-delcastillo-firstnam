from django.urls import path
from .views import recipes, recipe_one, recipe_two

urlpatterns = [
    path('list', recipes, name='list'),
    path('1', recipe_one, name="1"),
    path('2', recipe_two, name="2"),
]

app_name = 'ledger'