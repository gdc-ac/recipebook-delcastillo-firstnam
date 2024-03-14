from accounts.models import Profile
from django.db import models
from django.urls import reverse


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ledger:recipe-detail", args=[self.pk])


class Recipe(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return "Recipe {}".format(self.name)

    def get_absolute_url(self):
        return reverse("ledger:recipe-detail", args=[self.pk])

    author = models.ForeignKey(
        Profile, null=True, default=None, on_delete=models.CASCADE, related_name="users"
    )

    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)


class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100)
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE, related_name="recipe", default=1
    )

    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="ingredients", default=1
    )
