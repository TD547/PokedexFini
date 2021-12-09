from django.shortcuts import redirect, render
from json.decoder import JSONDecodeError
import json
import requests

from pokedex.models import Pokemon, PokemonDetailed, Team

# Create your views here.

def index(request):
    Pokemon.objects.all().delete()

    try:
        res = requests.get(
            "https://pokeapi.co/api/v2/pokemon?offset=0&limit=151",
            timeout=5
        )

        try:
            data = json.loads(res.text)
        except JSONDecodeError:
            data = None
            print("[ERROR]: No data.")

        try:
            if data != None:
                for pokemon in data['results']:
                    Pokemon(
                        pokemon.get("url").split('/')[6],
                        pokemon.get("name")
                    ).save()
                res.raise_for_status()
        except KeyError:
            Pokemon.objects.all().delete()

    except requests.exceptions.RequestException as err:
        print(err)

    pokemons = Pokemon.objects.all()

    return render(request, 'index.html', {
        'pokemons': pokemons
    })


def pokemon(request, id):
    PokemonDetailed.objects.all().delete()

    try:
        res = requests.get(
            "https://pokeapi.co/api/v2/pokemon/" + str(id),
            timeout=5
        )

        try:
            data = json.loads(res.text)
        except JSONDecodeError:
            data = None
            print("[ERROR]: No data.")

        try:
            if data != None:
                if len(data["types"]) > 1:
                    p_type = data["types"][0]["type"].get("name")
                    p_type += " "
                    p_type += data["types"][1]["type"].get("name")
                else:
                    p_type = data["types"][0]["type"].get("name")

                PokemonDetailed(
                    data.get("id"),
                    data.get("name"),
                    p_type,
                    data.get("height"),
                    data.get("weight"),
                    data["sprites"].get("front_default")
                ).save()
            res.raise_for_status()
        except KeyError:
            PokemonDetailed.objects.all().delete()

    except requests.exceptions.RequestException as err:
        print(err)

    pokemon = PokemonDetailed.objects.get(pk=id)

    return render(request, 'pokemon.html', {
        'pokemon': pokemon
    })


def team(request):
    pokemons = Pokemon.objects.all()
    team = []

    if 'team' not in request.session:
        team = ['None', 'None', 'None', 'None', 'None', 'None']

    try:
        for i in range(6):
            team.append(request.session["team"].get("pokemon-" + str(i)))
    except KeyError:
        request.session["team"] = [
            'None', 'None', 'None', 'None', 'None', 'None']
    except AttributeError:
        request.session["team"] = [
            'None', 'None', 'None', 'None', 'None', 'None']

    return render(request, 'team.html', {
        'team': team,
        'pokemons': pokemons,
        'range': range(6)
    })


def save_team(request):
    request.session["team"] = request.POST

    return redirect("/pokedex/team/")
