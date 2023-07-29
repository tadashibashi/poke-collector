from django.urls import path

from . import views

app_name = "main"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("pokemon/", views.PokemonList.as_view(), name="pokemon_index"),
    path("pokemon/create/", views.PokemonCreate.as_view(), name="pokemon_create"),
    path("pokemon/<int:pk>/update/", views.PokemonUpdate.as_view(), name="pokemon_update"),
    path("contests/<int:pk>/update/", views.contest_update, name="contest_update"),
    path("pokemon/<int:pk>/delete/", views.PokemonDelete.as_view(), name="pokemon_delete"),
    path("contests/<int:pk>/delete/", views.ContestDelete.as_view(), name="contest_delete"),
    path("pokemon/<int:pk>/", views.detail, name="pokemon_detail"),
    path("pokemon/<int:pk>/training/create", views.add_training, name="training_create"),
    path("contests/", views.ContestIndex.as_view(), name="contests_index"),
    path("contests/create/", views.ContestCreate.as_view(), name="contest_create"),
    path("pokemon/<int:poke_id>/contests/<int:contest_id>/associate", views.assoc_contest, name="assoc_contest"),
    path("pokemon/<int:poke_id>/contests/<int:contest_id>/disassociate", views.disassoc_contest, name="disassoc_contest"),
]
