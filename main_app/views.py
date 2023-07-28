from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

from .forms import PokemonForm, TrainingForm
from .models import Pokemon, Training


# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def detail(request, pk):
    pokemon = get_object_or_404(Pokemon, id=pk)
    return render(request, "detail.html", {
        "training_form": TrainingForm(),
        "pokemon": pokemon
    })


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

def add_training(request, pk):
    form = TrainingForm(request.POST)
    if form.is_valid():
        training = form.save(commit=False)
        training.pokemon_id = pk
        training.save()
    return redirect("main:pokemon_detail", pk=pk)

    

class PokemonList(ListView):
    model = Pokemon
    context_object_name = "pokelist"
    template_name = "pokemon/index.html"
