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
