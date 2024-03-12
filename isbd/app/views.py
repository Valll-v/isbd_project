from django.shortcuts import render
from django.views import View

from app.db import *
from app.serialization import *


def index(request):
    return render(request, "index.html")


def target_hero(request, hero_id):
    tuple_hero = get_target_hero(hero_id)
    body = {
        "hero": target_hero_to_dict(tuple_hero) if tuple_hero else None
    }
    return render(request, "target_hero.html", body)


class HeroesView(View):
    def get(self, request, *args, **kwargs):
        body = {
            "heroes": []
        }

        for hero in get_heroes_list():
            body["heroes"].append(tuple_to_hero(hero))

        return render(request, "heroes.html", body)


class MenacesView(View):
    def get(self, request, *args, **kwargs):
        body = {
            "menaces": []
        }

        for menace in get_menace_list():
            body["menaces"].append(tuple_to_menace(menace))

        return render(request, "menaces.html", body)


class TournamentsView(View):
    def get(self, request, *args, **kwargs):
        body = {
            "tournaments": []
        }

        for tournament in get_tournament_list():
            body["tournaments"].append(tuple_to_tournament(tournament))

        return render(request, "tournaments.html", body)
