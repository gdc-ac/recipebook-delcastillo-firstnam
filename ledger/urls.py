from django.urls import path

from .views import RecipeAddImgView, RecipeCreateView, RecipeListView, RecipesUpdateView

urlpatterns = [
    path("recipes/list", RecipeListView.as_view(), name="list"),
    path("recipe/add", RecipeCreateView.as_view()),
    path("recipe/<int:pk>", RecipesUpdateView.as_view(), name="recipe-detail"),
    path(
        "recipe/<int:pk>/add_image",
        RecipeAddImgView,
        name="recipe-detail-addimage",
    ),
]

app_name = "ledger"
