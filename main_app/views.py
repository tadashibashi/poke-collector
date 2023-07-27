from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

from .forms import PokemonForm
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

    def get_form_class(self):
        return PokemonForm

class PokemonUpdate(UpdateView):
    model = Pokemon
    fields = ["nickname", "moveset", "level"]
    def get_form_class(self):
        return PokemonForm


class PokemonDelete(DeleteView):
    model = Pokemon
    success_url = "/pokemon/"


class PokemonList(ListView):
    model = Pokemon
    context_object_name = "pokelist"
    template_name = "pokemon/index.html"
