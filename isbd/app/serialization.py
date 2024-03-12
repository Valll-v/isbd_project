from app.models import HeroProfile, Menace, Tournament


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


def target_hero_to_dict(hero_tuple):
    result = {
        "nickname": hero_tuple[0],
        "fullname": hero_tuple[1],
        "photo_url": hero_tuple[2],
        "death_date": hero_tuple[3],
        "rank": hero_tuple[4],
        "raiting": hero_tuple[5],
    }
    return result
