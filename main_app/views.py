from django.shortcuts import render, get_list_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, DetailView, ListView

from .models import Pokemon


# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

class PokemonDetail(DetailView):
    model = Pokemon
    template_name = "detail.html"

class PokemonCreate(CreateView):
    model = Pokemon
    fields = "__all__"
    success_url = "/pokemon/{id}"

class PokemonList(ListView):
    model = Pokemon
    context_object_name = "pokelist"
    template_name = "pokemon/index.html"

class pokemon:
    @staticmethod
    def create(request):
        # do create stuff here

        return HttpResponseRedirect(reverse("main:pokemon_index"))
