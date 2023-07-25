from django.urls import path

from . import views

app_name = "main"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("pokemon/", views.pokemon.index, name="pokemon_index"),
    path("pokemon/create/", views.pokemon.create, name="pokemon_create")
]
