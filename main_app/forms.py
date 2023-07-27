from django.forms import ModelForm, CharField
from django.forms.widgets import TextInput
from django.contrib.postgres.forms import SplitArrayWidget, SplitArrayField

from .models import Pokemon

class PokemonForm(ModelForm):
    moveset = SplitArrayField(CharField(max_length=64), 4, remove_trailing_nulls=True)
    class Meta:
        model = Pokemon
        fields = "__all__"
