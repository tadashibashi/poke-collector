from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

from .forms import PokemonForm, TrainingForm, ContestForm
from .models import Pokemon, Training, Contest


# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def detail(request, pk):
    pokemon = get_object_or_404(Pokemon, id=pk)

    contests_ids = pokemon.contest_set.all().values_list("id")
    contests_non_participant = Contest.objects.exclude(id__in=contests_ids)
    return render(request, "detail.html", {
        "training_form": TrainingForm(),
        "pokemon": pokemon,
        "contests_non_participant": contests_non_participant,
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

def assoc_contest(request, poke_id, contest_id):
    contest = get_object_or_404(Contest, id=contest_id)
    pokemon = get_object_or_404(Pokemon, id=poke_id)
    contest.pokemon.add(pokemon)
    return redirect("main:pokemon_detail", pk=poke_id)

def disassoc_contest(request, poke_id, contest_id):
    contest = get_object_or_404(Contest, id=contest_id)
    pokemon = get_object_or_404(Pokemon, id=poke_id)
    contest.pokemon.remove(pokemon)
    return redirect("main:pokemon_detail", pk=poke_id)

class ContestCreate(CreateView):
    model = Contest
    success_url = "/contests/"
    def get_form_class(self):
        return ContestForm

class ContestIndex(ListView):
    model = Contest
    template_name = "contest/index.html"
    context_object_name = "contests"

def contest_update(request, pk):
    contest = get_object_or_404(Contest, id=pk)
    print(contest.pokemon.all())
    if request.method == "GET":
        form = ContestForm(instance=contest)

        return render(request, "main_app/contest_form.html", {
            "contest": contest,
            "form": form
        })
    elif request.method == "POST":
        form = ContestForm(request.POST, instance=contest)
        if form.is_valid():
            form.save()
    return redirect("main:contests_index")


class ContestDelete(DeleteView):
    model = Contest
