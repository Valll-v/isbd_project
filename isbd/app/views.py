from django.shortcuts import render, redirect
from django.views import View
from django.db import IntegrityError
from django.db.utils import InternalError

from app.db import *
from app.serialization import *


def index(request):
    return render(request, "index.html")


def target_hero(request, hero_id):
    tuple_hero = get_target_hero(hero_id)
    body = {
        "hero": target_hero_to_dict(tuple_hero) if tuple_hero else None,
        "leader": check_leader(tuple_hero[6]),
    }
    return render(request, "target_hero.html", body)


def upgrade_hero_rank(request, hero_id):
    body = request.POST
    rank = body['hero_rank']
    if rank == 'C':
        new_rank = 'B'
    elif rank == 'B':
        new_rank = 'A'
    else:
        new_rank = 'S'
    upgrade_rank(hero_id, new_rank)
    return redirect("target-hero-view", hero_id=hero_id)


class PersonsView(View):
    def get(self, request, *args, **kwargs):
        body = {
            "persons": [],
        }
        post_serialize = {
            "journalist": "Журналист",
            "flyer": "Промоутер",
            "worker": "Рядовой сотрудник",
            "looker": "Смотритель",
            "director": "Директор подразделения",
            "technic": "Технический специалист",
            "cleaner": "Уборщик",
            "headhunter": "HR",
            "tournamental": "Турнирный специалист",
            "fighter": "Профессиональный боец",
            "security": "Охранник"
        }

        for person in get_persons_list():
            new_person = tuple_to_government_person(person)
            body["persons"].append(new_person)
            body["persons"][-1]["post"] = post_serialize[new_person["post"]]

        return render(request, "persons.html", body)


class HeroesView(View):
    def get(self, request, *args, **kwargs):
        body = {
            "heroes": []
        }

        for hero in get_heroes_list():
            hero = tuple_to_hero(hero)
            hero.leader = check_leader(hero.id)
            body["heroes"].append(hero)

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


class ExamsView(View):
    def get(self, request, *args, **kwargs):
        body = {
            "exams": []
        }

        for exam in get_exam_list():
            body["exams"].append(tuple_to_exam(exam))

        return render(request, "exams.html", body)


class CreateResultView(View):
    def get(self, request):
        return render(request, "create_result.html")

    def post(self, request):
        body = request.POST
        auth_id = int(body['auth_id'])
        exam_type = body['type']
        result = int(body['result'])
        inspector_id = body['inspector_id']
        try:
            create_result(auth_id, exam_type, result, inspector_id)
            return redirect("exam-results-view", auth_id=auth_id)
        except IntegrityError as e:
            if str(e).startswith('Не найден'):
                return render(request, "create_result.html",
                              {"error": 'Инспектор не найден, или у него нет прав'})
            return render(request, "create_result.html", {"error": "Не найдена регистрация на экзамен."})


class CreateHeroView(View):
    def get(self, request):
        return render(request, "make_hero.html")

    def post(self, request):
        body = request.POST
        print(body)
        person_id = int(body['person_id'])
        hero_nickname = body['hero_nickname']
        without_exam = True if body.get('without_exam') == 'on' else False
        extra_information = body['extra_information']
        try:
            create_hero(person_id, hero_nickname,
                        without_exam, extra_information)
            return redirect("heroes-view")
        except IntegrityError as e:
            e = 'Такой персоны не найдено!'
            return render(request, "make_hero.html", {"error": e})
        except InternalError:
            e = 'Не был сдан один или несколько этапов экзамена!'
            return render(request, "make_hero.html", {"error": e})


class CreateExamView(View):

    def get(self, request):
        return render(request, "create_exam.html")

    def post(self, request):
        body = request.POST
        person_id = int(body['person_id'])
        exam_time = body['datetime_exam']
        try:
            create_exam(person_id, exam_time)
            return redirect("exams-view")
        except IntegrityError:
            return render(request, "create_exam.html", {"error": True})


class ExamRegisterView(View):

    def get(self, request):
        return render(request, "exam_register.html")

    def post(self, request):
        body = request.POST
        person_id = int(body['person_id'])
        exam_id = int(body['exam_id'])
        try:
            create_exam_auth(person_id, exam_id)
            return redirect("exam-auths-view", exam_id=exam_id)
        except IntegrityError:
            return render(request, "exam_register.html", {"error": True})


class ExamAuthsView(View):
    def get(self, request, exam_id):
        body = {
            "exam_auths": []
        }

        for auth in get_exam_auths(exam_id):
            body["exam_auths"].append(tuple_to_auth(auth))

        return render(request, "exam_auths.html", body)


class TargetExamView(View):
    def get(self, request, *args, **kwargs):
        body = {}
        return render(request, "target_exam.html", body)


class ExamResultsView(View):
    def get(self, request, auth_id):
        body = {
            "exam_results": []
        }

        for result in get_exam_results(auth_id):
            body["exam_results"].append(tuple_to_result(result))

        return render(request, "exam_results.html", body)


class UpdateRankView(View):
    def get(self, request):
        return render(request, "update_rank.html")

    def post(self, request):
        body = request.POST
        hero_id = int(body['hero_id'])
        rank = body['rank']
        rating = int(body['rating'])
        try:
            create_or_update_rank(hero_id, rank, rating)
            return redirect("target-hero-view", hero_id=hero_id)
        except IntegrityError as e:
            return render(request, "update_rank.html", {"error": e})
