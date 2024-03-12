import psycopg2
from urllib.request import urlopen
import csv
import string
import random
from tabulate import tabulate


HEROES = 'data/heroes.csv'
VILLAINS = 'data/villains.csv'
OTHER = 'data/others.csv'
DOJOS = 'data/dojos.csv'
POSTS = 'data/posts.csv'
PERM = 'data/permissions.csv'
BLACKLISTS = 'data/blacklists.csv'


MENACE_LEVELS = [
    'tiger',
    'demon',
    'dragon',
    'god',
]
MENACE_STATUSES = [
    'death',
    'alive',
    'hidden',
]
T_STATUSES = [
    'announced',
    'progress',
    'finished',
    'canceled',
]
TOWNS_ID = []
PERSONS_ID = []
HEROES_ID = []
VILLAINS_ID = []
DOJOS_ID = []
GOV_ID = []
PERM_ID = []
TOURNAMENT_AUTH_ID = []


def read_csv_link(url):
    response = urlopen(url)
    lines = [line.decode('utf-8') for line in response.readlines()]
    reader = csv.reader(lines, delimiter=';')
    header = 1
    for row in reader:
        if header:
            header = 0
        else:
            yield row


def read_csv_file(filepath):
    with open(filepath, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=',')
        header = 1
        for row in reader:
            if row:
                if header:
                    header = 0
                else:
                    yield row


class Cursor:
    def __init__(self):
        conn = psycopg2.connect(
            database="studs", user='s336775',
            password='Tojb3TW78eDWGcuC', host='127.0.0.1',
            port='5432'
        )
        conn.autocommit = True
        self.cursor = conn.cursor()

    def execute(self, query):
        self.cursor.execute(query)

    def fetchone(self):
        return self.cursor.fetchone()

    def fetchall(self):
        return self.cursor.fetchall()

    def pretty_result(self):
        rows = self.fetchall()
        columns = [desc[0] for desc in self.cursor.description]
        print(tabulate(rows, headers=columns))


def create_towns(cursor: Cursor):
    for s in string.ascii_uppercase:
        query = f"INSERT INTO town VALUES (DEFAULT, '{s}') RETURNING town.id;"
        try:
            cursor.execute(query)
            TOWNS_ID.append(cursor.fetchone()[0])
        except Exception as e:
            print(e)


def create_villains(cursor: Cursor):
    for villain in read_csv_file(VILLAINS):
        try:
            query = f'''
            INSERT INTO 
                menace 
            VALUES 
                (DEFAULT, '{villain[2]}', '{villain[1]}',
                '{random.choice(MENACE_LEVELS)}', '2021-01-01', 
                {random.choice(TOWNS_ID)}, NULL,
                '{random.choice(MENACE_STATUSES)}', false, NULL)
            RETURNING menace.id;
            '''
            cursor.execute(query)
            VILLAINS_ID.append(cursor.fetchone()[0])
        except Exception as e:
            print(e)


def create_heroes(cursor: Cursor):
    for hero in read_csv_file(HEROES):
        try:
            query = f'''
            INSERT INTO 
                person 
            VALUES 
                (DEFAULT, '{hero[3]}', {random.choice(TOWNS_ID)}, 
                NULL, NULL, NULL)
            RETURNING person.id;
            '''
            cursor.execute(query)
            person_id = cursor.fetchone()[0]
            PERSONS_ID.append(person_id)
            query = f'''
            INSERT INTO 
                hero_profile 
            VALUES 
                (DEFAULT, '{person_id}', NULL, '{hero[3]}',
                '2021-01-01', NULL, true, NULL, NULL)
            RETURNING hero_profile.id;
            '''
            cursor.execute(query)
            hero_id = cursor.fetchone()[0]
            HEROES_ID.append(hero_id)
            query = f'''
            INSERT INTO 
                ranking 
            VALUES 
                (DEFAULT, '{hero_id}', '{random.choice(['S', 'A', 'B', 'C'])}', 
                100000, '2021-01-01', NULL, true);
            '''
            cursor.execute(query)
        except Exception as e:
            print(e)


def create_dojos(cursor):
    for dojo in read_csv_file(DOJOS):
        try:
            query = f'''
            INSERT INTO 
                dojo 
            VALUES 
                (DEFAULT, '{dojo[0]}', {random.choice(PERSONS_ID)})
            RETURNING dojo.id;
            '''
            cursor.execute(query)
            DOJOS_ID.append(cursor.fetchone()[0])
        except Exception as e:
            print(e)


def create_gov(cursor: Cursor):
    posts = [post[0] for post in read_csv_file(POSTS)]
    for gov in read_csv_file(OTHER):
        try:
            query = f'''
            INSERT INTO 
                person 
            VALUES 
                (DEFAULT, '{gov[2]}', {random.choice(TOWNS_ID)}, NULL, NULL, NULL)
            RETURNING person.id;
            '''
            cursor.execute(query)
            person_id = cursor.fetchone()[0]
            PERSONS_ID.append(person_id)
            query = f'''
            INSERT INTO 
                goverment_profile 
            VALUES 
                (DEFAULT, '{person_id}', '{random.choice(posts)}', '2021-01-01')
            RETURNING goverment_profile.id;
            '''
            cursor.execute(query)
            GOV_ID.append(cursor.fetchone()[0])
        except Exception as e:
            print(e)


def create_perms(cursor):
    for perm in read_csv_file(PERM):
        try:
            query = f'''
            INSERT INTO 
                permission 
            VALUES 
                (DEFAULT, '{perm[0]}', '2021-01-01', 
                'smth')
            RETURNING permission.id;
            '''
            cursor.execute(query)
            perm_id = cursor.fetchone()[0]
            PERM_ID.append(perm_id)
            for gov in random.choices(GOV_ID, k=5):
                try:
                    query = f'''
                    INSERT INTO 
                        permission_goverment_profile 
                    VALUES 
                        ({perm_id}, {gov})
                    ;
                    '''
                    cursor.execute(query)
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)


def create_black(cursor: Cursor):
    for black in read_csv_file(BLACKLISTS):
        try:
            query = f'''
            INSERT INTO 
                person 
            VALUES 
                (DEFAULT, '{black[1]}', {random.choice(TOWNS_ID)}, NULL, NULL, NULL)
            RETURNING person.id;
            '''
            cursor.execute(query)
            person_id = cursor.fetchone()[0]
            PERSONS_ID.append(person_id)
            query = f'''
            INSERT INTO 
                blacklist 
            VALUES 
                (DEFAULT, '{person_id}', 'why president in OPM???', '2021-01-01')
            ;
            '''
            cursor.execute(query)
        except Exception as e:
            print(e)


def create_exams(cursor):
    for i in range(10):
        try:
            query = f'''
            INSERT INTO 
                exam 
            VALUES 
                (DEFAULT, {random.choice(GOV_ID)}, '2021-01-01', NULL, NULL)
            RETURNING exam.id;
            '''
            cursor.execute(query)
            exam = cursor.fetchone()[0]
            for t in range(10):
                query = f'''
                INSERT INTO 
                    exam_auth 
                VALUES 
                    (DEFAULT, {random.choice(PERSONS_ID)}, {exam}, '2021-01-01',
                     NULL, NULL)
                RETURNING exam_auth.id;
                '''
                cursor.execute(query)
                exam_auth = cursor.fetchone()[0]
                for ty in ('phys', 'intelligent'):
                    query = f'''
                    INSERT INTO 
                        exam_result 
                    VALUES 
                        (DEFAULT, {exam_auth}, '{ty}', {50}, 
                        {random.choice(GOV_ID)})
                    ;
                    '''
                    cursor.execute(query)
        except Exception as e:
            print(e)


def create_tournaments(cursor):
    for i in range(10):
        try:
            query = f'''
            INSERT INTO 
                tournament 
            VALUES 
                (DEFAULT, '2021-01-01', '{random.choice(T_STATUSES)}', 
                NULL, {random.choice(GOV_ID)})
            RETURNING tournament.id;
            '''
            cursor.execute(query)
            tournament = cursor.fetchone()[0]
            for t in range(10):
                try:
                    query = f'''
                    INSERT INTO 
                        tournament_auth 
                    VALUES 
                        (DEFAULT, {random.choice(PERSONS_ID)}, {tournament}, 
                        'undefined', NULL, NULL)
                    RETURNING tournament_auth.id;
                    '''
                    cursor.execute(query)
                    tournament_auth = cursor.fetchone()[0]
                    TOURNAMENT_AUTH_ID.append(tournament_auth)
                except Exception as e:
                    print(e)
            for _ in range(20):
                fighters = random.choices(TOURNAMENT_AUTH_ID, k=2)
                query = f'''
                INSERT INTO 
                    tournament_fight 
                VALUES 
                    (DEFAULT, {fighters[0]}, {fighters[1]}, 
                    '{random.choice(['w1', 'w2'])}', 'finished')
                ;
                '''
                cursor.execute(query)
        except Exception as e:
            print(e)


def trunc(cursor: Cursor):
    try:
        query = 'TRUNCATE TABLE town CASCADE;'
        cursor.execute(query)
    except Exception as e:
        print(e)


def select_heroes(cursor: Cursor):
    try:
        query = 'SELECT * FROM hero_profile;'
        cursor.execute(query)
        print(cursor.pretty_result())
    except Exception as e:
        print(e)


def select_villains(cursor: Cursor):
    try:
        query = 'SELECT * FROM menace;'
        cursor.execute(query)
        print(cursor.pretty_result())
    except Exception as e:
        print(e)


def select_dojos(cursor: Cursor):
    try:
        query = 'SELECT * FROM dojo;'
        cursor.execute(query)
        print(cursor.pretty_result())
    except Exception as e:
        print(e)


def select_govs(cursor: Cursor):
    try:
        query = 'SELECT * FROM goverment_profile;'
        cursor.execute(query)
        print(cursor.pretty_result())
    except Exception as e:
        print(e)


def select_results(cursor: Cursor):
    try:
        query = 'SELECT * FROM exam_result;'
        cursor.execute(query)
        print(cursor.pretty_result())
    except Exception as e:
        print(e)


def select_black(cursor: Cursor):
    try:
        query = 'SELECT * FROM blacklist;'
        cursor.execute(query)
        print(cursor.pretty_result())
    except Exception as e:
        print(e)


def select_fights(cursor: Cursor):
    try:
        query = 'SELECT * FROM tournament_fight;'
        cursor.execute(query)
        print(cursor.pretty_result())
    except Exception as e:
        print(e)


def main():
    cursor = Cursor()
    create_towns(cursor)
    create_heroes(cursor)
    create_dojos(cursor)
    create_villains(cursor)
    create_gov(cursor)
    create_perms(cursor)
    create_exams(cursor)
    create_black(cursor)
    create_tournaments(cursor)


if __name__ == '__main__':
    main()
