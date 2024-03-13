from app.models import HeroProfile, Menace, Tournament, Person, Exam, ExamAuth, ExamResult


def tuple_to_auth(auth_tuple):
    auth_profile = ExamAuth()
    for i, key in enumerate(auth_profile.__dict__):
        if key != '_state':
            auth_profile.__setattr__(key, auth_tuple[i - 1])
    return auth_profile


def tuple_to_government_person(person_tuple):
    result = {
        "id": person_tuple[0],
        "fullname": person_tuple[1],
        "photo_url": person_tuple[2],
        "post": person_tuple[3]
    }
    return result


def tuple_to_exam(exam_tuple):
    exam_profile = Exam()
    for i, key in enumerate(exam_profile.__dict__):
        if key != '_state':
            exam_profile.__setattr__(key, exam_tuple[i - 1])
    return exam_profile


def tuple_to_hero(hero_tuple):
    hero_profile = HeroProfile()
    for i, key in enumerate(hero_profile.__dict__):
        if key != '_state':
            hero_profile.__setattr__(key, hero_tuple[i - 1])
    return hero_profile


def tuple_to_menace(menace_tuple):
    menace = Menace()
    for i, key in enumerate(menace.__dict__):
        if key != '_state':
            menace.__setattr__(key, menace_tuple[i - 1])
    return menace


def tuple_to_tournament(tournament_tuple):
    tournament = Tournament()
    for i, key in enumerate(tournament.__dict__):
        if key != '_state':
            tournament.__setattr__(key, tournament_tuple[i - 1])
    return tournament


def tuple_to_result(result_tuple):
    result = ExamResult()
    for i, key in enumerate(result.__dict__):
        if key != '_state':
            result.__setattr__(key, result_tuple[i - 1])
    return result


def target_hero_to_dict(hero_tuple):
    result = {
        "nickname": hero_tuple[0],
        "fullname": hero_tuple[1],
        "photo_url": hero_tuple[2],
        "death_date": hero_tuple[3],
        "rank": hero_tuple[4],
        "raiting": hero_tuple[5],
        "id": hero_tuple[6]
    }
    return result
