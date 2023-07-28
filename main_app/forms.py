from django.forms import ModelForm, CharField
from django.contrib.postgres.forms import SplitArrayField

from .models import Pokemon, Training


class PokemonForm(ModelForm):
    moveset = SplitArrayField(CharField(max_length=64), 4, remove_trailing_nulls=True)
    class Meta:
        model = Pokemon
        fields = "__all__"

class TrainingForm(ModelForm):
    class Meta:
        model = Training
        fields = ["activity", "exp_points", "date"]