-- Дополнительные ограничения для обеспечения целостности

-- При удалении Додзё принадлежность к нему человека обнуляется (on delete set null)
alter table person
    drop constraint person_dojo_id_fkey,
    add constraint check_dojo_exists
        foreign key (dojo_id) references dojo (id) on delete set null;

-- В профиле героя edit_date >= auth_date
alter table hero_profile
    add constraint profile_timestamp_chronology
        check ( edit_date >= auth_date);

-- Дата регистрации на экзамен не меньше даты его отмены
alter table exam_auth
    add constraint exam_timestamp_chronology
        check ( auth_date <= cancel_date);

-- Боец не может сражаться сам с собой на турнире
alter table tournament_fight
    add constraint different_fighters
        check ( left_id != right_id );


-- При удалении угрозы удаляется и отчет об этой угрозе menace_record (вся строка по menace_id)
alter table menace_record
    drop constraint menace_record_menace_id_fkey,
    add constraint check_menace_exist
        foreign key (menace_id) references menace (id) on delete cascade ;

-- При удалении турнирного боя удаляется и отчет этого боя tournament_fight_record (вся строка по fight_id хз как это сделать, выяснить)
alter table tournament_fight_record
    drop constraint tournament_fight_record_fight_id_fkey,
    add constraint check_fight_exists
        foreign key (fight_id) references tournament_fight (id) on delete cascade;

-- У вебсайтов героев уникальные url, которые имеют ограничение на формат
-- http://heroes/onepunchman.com
alter table hero_profile
    add constraint check_regex_constraint
        check (hero_profile.website_url ~ '\/heroes\/([a-z0-9_\.\-]+)');

-- У фотографий людей уникальные url, которые имеют ограничение на формат
-- http://people/ahmed123.jpg
alter table person
    add constraint check_regex_constraint
        check (person.photo_url ~ '\/media\/persons\/([a-z0-9_\.\-]+).jpg$');
