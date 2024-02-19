CREATE TYPE menace_status AS ENUM (
	'death',
	'alive',
	'hidden'
);

CREATE TYPE hero_fight_status AS ENUM (
	'announced',
	'progress',
	'win',
	'lost'
);

CREATE TYPE tournament_status AS ENUM (
	'announced',
	'progress',
	'finished',
	'canceled'
);

CREATE TYPE menace_level AS ENUM (
	'tiger',
	'demon',
	'dragon',
	'god'
);

CREATE TYPE exam_result_type AS ENUM (
	'phys',
	'intelligent'
);

CREATE TYPE tournament_fight_status AS ENUM (
	'announced',
	'progress',
	'finished'
);

CREATE TYPE tournament_fight_result AS ENUM (
	'w1',
	'w2'
);

CREATE TABLE town
(
	id SERIAL PRIMARY KEY,
	code VARCHAR(1) UNIQUE
);

CREATE TABLE dojo
(
    id SERIAL PRIMARY KEY,
    name VARCHAR(32) UNIQUE,
    leader_id INTEGER
);

CREATE TABLE person
(
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(32) NOT NULL,
    town_id INTEGER NOT NULL,
    photo_url VARCHAR(2083) UNIQUE,
    death_date TIMESTAMP,
    dojo_id INTEGER
);

CREATE TABLE goverment_profile
(
    id SERIAL PRIMARY KEY,
    person_id INTEGER NOT NULL,
    post VARCHAR(32) NOT NULL,
    start_date TIMESTAMP NOT NULL
);

CREATE TABLE permission
(
    id SERIAL PRIMARY KEY,
    description VARCHAR(32) NOT NULL,
    creation_date TIMESTAMP NOT NULL,
    special VARCHAR(64) DEFAULT NULL
);

CREATE TABLE permission_goverment_profile
(
    permission_id INTEGER NOT NULL,
    goverment_employee_id INTEGER NOT NULL,
    PRIMARY KEY (permission_id, goverment_employee_id)
);

CREATE TABLE exam
(
    id SERIAL PRIMARY KEY,
    responsible_id INTEGER NOT NULL,
    exam_date TIMESTAMP NOT NULL,
    cancel_date TIMESTAMP,
    cancel_reason VARCHAR(100)
);

CREATE TABLE exam_auth
(
    id SERIAL PRIMARY KEY,
    person_id INTEGER NOT NULL,
    exam_id INTEGER NOT NULL,
    auth_date TIMESTAMP NOT NULL,
    cancel_date TIMESTAMP,
    cancel_reason VARCHAR(100)
);

CREATE TABLE exam_result
(
    id SERIAL PRIMARY KEY,
    auth_id INTEGER NOT NULL,
    type exam_result_type,
    result INTEGER NOT NULL,
    inspector_id INTEGER NOT NULL
);

CREATE TABLE hero_profile
(
    id SERIAL PRIMARY KEY,
    person_id INTEGER UNIQUE,
    exam_auth_id INTEGER,
    nickname VARCHAR(30) UNIQUE,
    auth_date TIMESTAMP NOT NULL,
    edit_date TIMESTAMP,
    without_exam BOOL DEFAULT FALSE,
    extra_information VARCHAR(1024),
    website_url VARCHAR(2083) UNIQUE
);

CREATE TABLE ranking
(
    id SERIAL PRIMARY KEY,
    hero_id INTEGER NOT NULL,
    rank VARCHAR(1) NOT NULL,
    raiting INTEGER DEFAULT NULL,
    creation_date TIMESTAMP NOT NULL,
    edit_date TIMESTAMP,
    actual BOOL DEFAULT TRUE
);

CREATE TABLE blacklist
(
    id SERIAL PRIMARY KEY,
    person_id INTEGER NOT NULL,
    reason VARCHAR(100) NOT NULL,
    auth_date TIMESTAMP NOT NULL
);

CREATE TABLE menace
(
    id SERIAL PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    description VARCHAR(100) DEFAULT NULL,
    "level" menace_level,
    view_date TIMESTAMP NOT NULL,
    view_town_id INTEGER NOT NULL,
    current_town_id INTEGER,
    status menace_status,
    from_blacklist BOOL DEFAULT FALSE,
    blacklist_id INTEGER
);

CREATE TABLE menace_record
(
    id SERIAL PRIMARY KEY,
    responsible_id INTEGER NOT NULL,
    menace_id INTEGER NOT NULL,
    info VARCHAR(512) NOT NULL,
    creation_date TIMESTAMP NOT NULL
);

CREATE TABLE hero_fight
(
    id SERIAL PRIMARY KEY,
    menace_id INTEGER NOT NULL,
    hero_id INTEGER NOT NULL,
    status hero_fight_status
);

CREATE TABLE fight_record
(
    id SERIAL PRIMARY KEY,
    responsible_id INTEGER NOT NULL,
    hero_fight_id INTEGER NOT NULL,
    info VARCHAR(100) DEFAULT NULL,
    creation_date TIMESTAMP NOT NULL
);

CREATE TABLE "action"
(
    id SERIAL PRIMARY KEY,
    hero_id INTEGER NOT NULL,
    responsible_id INTEGER NOT NULL,
    description VARCHAR(100) DEFAULT NULL,
    money INTEGER NOT NULL,
    hero_fight_id INTEGER
);

CREATE TABLE tournament
(
    id SERIAL PRIMARY KEY,
    date TIMESTAMP NOT NULL,
    description VARCHAR(100) DEFAULT NULL,
    status tournament_status,
    responsible_id INTEGER NOT NULL
);

CREATE TABLE tournament_auth
(
    id SERIAL PRIMARY KEY,
    person_id INTEGER UNIQUE,
    tournament_id INTEGER NOT NULL,
    style VARCHAR(32) NOT NULL,
    cancel_date TIMESTAMP DEFAULT NULL,
    cancel_reason VARCHAR(100) DEFAULT NULL
);

CREATE TABLE rank_record
(
    id SERIAL PRIMARY KEY,
    person_id INTEGER NOT NULL,
    auth_id INTEGER NOT NULL,
    description VARCHAR(100) DEFAULT NULL,
    mark INTEGER NOT NULL
);

CREATE TABLE tournament_fight
(
    id SERIAL PRIMARY KEY,
    left_id INTEGER NOT NULL,
    right_id INTEGER NOT NULL,
    result tournament_fight_result,
    status tournament_fight_status
);

CREATE TABLE tournament_fight_record
(
    id SERIAL PRIMARY KEY,
    responsible_id INTEGER NOT NULL,
    fight_id INTEGER NOT NULL,
    info VARCHAR(100) NOT NULL,
    creation_date TIMESTAMP NOT NULL
);
