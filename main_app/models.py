from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse

def get_empty_moveset():
    return ["" for i in range(4)]

# Create your models here.
class Pokemon(models.Model):
    number = models.IntegerField()
    nickname = models.CharField(max_length=100)
    level = models.IntegerField()
    moveset = ArrayField(models.CharField(max_length=64, default=str), size=4, default=list)

    def get_moveset(self):
        return ",".split(self.moveset)

    def __str__(self):
        return self.nickname

    def get_absolute_url(self):
        return reverse("main:pokemon_detail", kwargs={"pk": self.id})

