from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from .forms import RecipeForm, RecipeImageForm
from .models import Recipe, RecipeImage


class RecipeListView(ListView):
    model = Recipe
    template_name = "list.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["form"] = RecipeForm()
        return ctx

    def post(self, request, *args, **kwargs):
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = Recipe()
            recipe.name = form.cleaned_data.get("name")
            recipe.author = form.cleaned_data.get("author")
            recipe.save()
            return self.get(request, *args, **kwargs)
        else:
            self.object_list = self.get_queryset(**kwargs)
            context = self.get_context_data(**kwargs)
            context["form"] = form
            return self.render_to_response(context)


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "recipe_create.html"

    def get_success_url(self):
        return reverse_lazy("recipes:list")


class RecipesUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "recipe_detail.html"


def RecipeAddImgView(request, pk):
    form = RecipeImageForm()

    if request.method == "POST":
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            recipe_img = RecipeImage()
            recipe_img.image = form.cleaned_data.get("image")
            recipe_img.description = form.cleaned_data.get("description")
            recipe_img.recipe = Recipe.objects.get(pk=pk)
            recipe = recipe_img.recipe
            recipe_img.save()
            return redirect("ledger:recipe-detail", pk=recipe.pk)

    ctx = {"form": form, "recipe": Recipe.objects.get(pk=pk)}

    return render(request, "recipe_addimage.html", ctx)

    # def get_context_data(self, **kwargs):
    #     ctx = super().get_context_data(Recipe.objects.get(self.kwargs["pk"]))
    #     ctx["form"] = RecipeImageForm()
    #     return ctx

    # def post(self, request, *args, **kwargs):
    #     form = RecipeImageForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         recipe_img = RecipeImage()
    #         recipe_img.image = form.cleaned_data.get("image")
    #         recipe_img.description = form.cleaned_data.get("description")
    #         recipe_img.recipe = form.cleaned_data.get("recipe")
    #         recipe_img.save()q
    #         return self.get(request, *args, **kwargs)
    #     else:
    #         context = self.get_context_data(**kwargs)
    #         context["form"] = form
    #         return self.render_to_response(context)

    # def get_success_url(self):
    #     return reverse_lazy("recipe-detail", kwargs={"pk": self.object.pk})
