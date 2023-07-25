from django.shortcuts import render, get_list_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect


# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

poke_db = [
    {
        "name": "Pikachu", "no": 25, "types": ["electric"],
        "moves": ["thundershock", "tackle", "growl"],
        "height": "1' 4\"", "weight_lbs": 13,
        "evolves_from": 172, "evolves_to": 26,
    },
    {
        "name": "Charizard", "no": 6, "types": ["fire", "flying"],
        "moves": ["fire blast", "fire spin", "flamethrower", "seismic toss"],
        "height": "5' 7\"", "weight_lbs": 200,
        "evolves_from": 5, "evolves_to": -1,
    }
]


class pokemon:
    @staticmethod
    def index(request):
        return render(request, "pokemon/index.html", {"pokemon": poke_db})


    @staticmethod
    def create(request):
        # do create stuff here

        return HttpResponseRedirect(reverse("main:pokemon_index"))
