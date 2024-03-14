from django.contrib import admin

from .models import Recipe, RecipeIngredient


class RecipeIngInline(admin.TabularInline):
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngInline]


admin.site.register(Recipe, RecipeAdmin)

# user: dell
# password: coolwithyou
