from django.contrib import admin

from .models import Recipe, RecipeImage, RecipeIngredient


class RecipeIngrInline(admin.TabularInline):
    model = RecipeIngredient


class RecipeImgInline(admin.TabularInline):
    model = RecipeImage


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngrInline, RecipeImgInline]


admin.site.register(Recipe, RecipeAdmin)

# user: dell
# password: coolwithyou
