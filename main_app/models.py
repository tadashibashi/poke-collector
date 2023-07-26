from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse


# Create your models here.
class Pokemon(models.Model):
    number = models.IntegerField()
    nickname = models.CharField(max_length=100)
    moveset = ArrayField(models.CharField(64), size=4)
    level = models.IntegerField()

    def __str__(self):
        return self.nickname

    def get_absolute_url(self):
        return reverse("main:pokemon_detail", kwargs={"pk": self.id})

