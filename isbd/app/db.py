from datetime import datetime

from django.db import connection
from django.db import IntegrityError


def get_persons_list():
    with connection.cursor() as cursor:
        query = """
            SELECT p.id, p.fullname, p.photo_url, gp.post
            FROM person AS p
            JOIN goverment_profile as gp
            ON gp.person_id = p.id
        """
        print(query)
        cursor.execute(query)
        return cursor.fetchall()


def get_heroes_list():
    with connection.cursor() as cursor:
        query = """
            SELECT * FROM hero_profile;
        """
        print(query)
        cursor.execute(query)
        return cursor.fetchall()


def get_menace_list():
    with connection.cursor() as cursor:
        query = """
            SELECT * FROM menace;
        """
        print(query)
        cursor.execute(query)
        return cursor.fetchall()


def get_tournament_list():
    with connection.cursor() as cursor:
        query = """
            SELECT * FROM tournament;
        """
        print(query)
        cursor.execute(query)
        return cursor.fetchall()


def upgrade_rank(hero_id, new_rank):
    with connection.cursor() as cursor:
        query = f"""
            UPDATE ranking SET rank = '{new_rank}', raiting = 0
            WHERE hero_id = {hero_id};
        """
        print(query)
        cursor.execute(query)



def get_target_hero(hero_id):
    with connection.cursor() as cursor:
        query = f"""
            SELECT 
                h.nickname, p.fullname, p.photo_url, 
                p.death_date, r.rank, r.raiting, h.id
            FROM hero_profile as h
            JOIN person as p ON p.id = h.person_id
            JOIN ranking as r ON r.hero_id = h.id
            WHERE h.id = {hero_id}
            LIMIT 1;
        """
        print(query)
        cursor.execute(query)
        return cursor.fetchone()


def get_exam_list():
    with connection.cursor() as cursor:
        query = """
            SELECT * FROM exam
            WHERE exam_date > NOW()
            AND cancel_date IS NULL;
        """
        print(query)
        cursor.execute(query)
        return cursor.fetchall()


def get_exam_auths(exam_id):
    with connection.cursor() as cursor:
        query = f"""
            SELECT * FROM exam_auth AS ea
            LEFT JOIN hero_profile as hp
            ON hp.person_id = ea.person_id
            WHERE exam_id = {exam_id} and hp.id IS NULL
            ORDER  BY ea.id DESC;
        """
        print(query)
        cursor.execute(query)
        result = cursor.fetchall()
        return result


def get_exam_results(auth_id):
    with connection.cursor() as cursor:
        query = f"""
            SELECT * FROM exam_result
            WHERE auth_id = {auth_id};
        """
        print(query)
        cursor.execute(query)
        return cursor.fetchall()


def create_exam(person_id, exam_time):
    with connection.cursor() as cursor:
        query = f"""
                    SELECT gp.id FROM person AS p
                    JOIN goverment_profile AS gp
                    ON gp.person_id = p.id
                    JOIN permission_goverment_profile AS pgp
                    ON pgp.goverment_employee_id = gp.id
                    JOIN permission AS pg
                    ON pgp.permission_id = pg.id
                    WHERE p.id = {person_id}
                    AND (pg.description = 'tournaments' 
                    OR pg.description = 'all');
                """
        print(query)
        cursor.execute(query)
        persons = cursor.fetchall()
        if not persons:
            raise IntegrityError
        query = f"""
            INSERT INTO exam
            VALUES (DEFAULT, {persons[0][0]}, '{exam_time}', NULL, NULL);
        """
        print(query)
        cursor.execute(query)


def create_exam_auth(person_id, exam_id):
    with connection.cursor() as cursor:
        query = f"""
            INSERT INTO exam_auth
            VALUES (DEFAULT, {person_id}, {exam_id}, NOW(), NULL, NULL);
        """
        print(query)
        cursor.execute(query)


def create_hero(person_id, hero_nickname, without_exam, extra_information):
    with connection.cursor() as cursor:
        query = f"""
            CALL checkExamToAddHeroProfile(
                {person_id},
                '{hero_nickname}',
                '{datetime.now()}',
                {without_exam},
                '{extra_information}'
            );
        """
        print(query)
        cursor.execute(query)


def create_result(auth_id, result_type, exam_result, inspector_id):
    with connection.cursor() as cursor:
        query = f"""
            SELECT id FROM goverment_profile
            WHERE person_id = {inspector_id};
        """
        print(query)
        cursor.execute(query)
        result = cursor.fetchall()
        if not result:
            raise IntegrityError('Не найден такой инспектор')
        inspector_id = result[0][0]
        query = f"""
            INSERT INTO exam_result VALUES (
                DEFAULT, {auth_id}, '{result_type}', {exam_result}, {inspector_id}
            )
        """
        print(query)
        cursor.execute(query)


def create_or_update_rank(hero_id, rank, rating):
    with connection.cursor() as cursor:
        query = f"""
            UPDATE ranking SET rank = '{rank}', raiting = {rating}
            WHERE hero_id = {hero_id};
        """
        print(query)
        cursor.execute(query)


def check_leader(hero_id):
    with connection.cursor() as cursor:
        query = f"""
            SELECT r.rank FROM hero_profile as hp 
            JOIN ranking as r
            ON r.hero_id = hp.id
            WHERE hp.id = {hero_id}
        """
        print(query)
        cursor.execute(query)
        result = cursor.fetchall()
        if not result:
            return False
        result = result[0][0]
        query = f"""
            SELECT hero_id FROM ranking 
            WHERE rank = '{result}'
            ORDER BY raiting DESC
            LIMIT 1;
        """
        print(query)
        cursor.execute(query)
        result = cursor.fetchall()
        return hero_id == result[0][0]
