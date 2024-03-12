from django.db import connection


def get_heroes_list():
    with connection.cursor() as cursor:
        query = """
            SELECT * FROM hero_profile;
        """
        cursor.execute(query)
        return cursor.fetchall()


def get_menace_list():
    with connection.cursor() as cursor:
        query = """
            SELECT * FROM menace;
        """
        cursor.execute(query)
        return cursor.fetchall()


def get_tournament_list():
    with connection.cursor() as cursor:
        query = """
            SELECT * FROM tournament;
        """
        cursor.execute(query)
        return cursor.fetchall()


def get_target_hero(hero_id):
    with connection.cursor() as cursor:
        query = f"""
            SELECT 
                h.nickname, p.fullname, p.photo_url, 
                p.death_date, r.rank, r.raiting
            FROM hero_profile as h
            JOIN person as p ON p.id = h.person_id
            JOIN ranking as r ON r.hero_id = h.id
            WHERE h.id = {hero_id}
            LIMIT 1;
        """
        cursor.execute(query)
        return cursor.fetchone()
