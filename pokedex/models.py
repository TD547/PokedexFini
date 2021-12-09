from django.db import models

# Create your models here.


class Team(models.Model):
    pokemons = models.CharField(max_length=4096, default=None)

    def __str__(self):
        return self.pokemons


class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class PokemonDetailed(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)
    p_type = models.CharField(max_length=256)
    p_height = models.IntegerField()
    p_weight = models.IntegerField()
    p_image = models.URLField()
    p_isInTeam = models.BooleanField(default=False)

    def __str__(self):
        return self.name
