-- Триггеры вызываются до или после обработки событий UPDATE, INSERT ли DELETE

-- При добавлении или изменении записи menace проверить, что при from_blacklist == false, blacklist_id == null
create or replace function change_from_blacklist_trigger()
    returns trigger as $$
begin
    if new.from_blacklist is false and new.blacklist_id is not null then
        new.blacklist_id := null;
    end if;
    return new;
end $$ language plpgsql;

create trigger change_from_blacklist
    before update or insert on menace for each row
    execute function change_from_blacklist_trigger();


-- При добавлении или изменении записи hero_profile проверить, что при without_exam == true, exam_auth_id == null
create or replace function change_without_exam_trigger()
    returns trigger as $$
begin
    if new.without_exam is true and new.exam_auth_id is not null then
        new.exam_auth_id := null;
    end if;

    return new;
end $$ language plpgsql;

create trigger change_from_blacklist
    before update or insert on hero_profile for each row
    execute function change_without_exam_trigger();


-- При изменении записей hero_profile и ranking их поля edit_date будут принимать текущее время
create or replace function set_edit_date_trigger()
    returns trigger as $$
begin
    new.edit_date := CURRENT_TIMESTAMP;
    return new;
end $$ language plpgsql;

create trigger set_hero_profile_edit_date
    before update on hero_profile for each row
    execute function set_edit_date_trigger();

create trigger set_ranking_edit_date
    before update on ranking for each row
    execute function set_edit_date_trigger();





-- При добавлении записи person поле photo_url заполняется на основе fullname и id человека
create or replace function set_photo_url_trigger()
    returns trigger as $$
begin
    new.photo_url := concat('http://localhost:8888/media/', lower(new.fullname), new.id, '.jpg');
    return new;
end $$ language plpgsql;

create trigger set_photo_url
    before insert on person for each row
    execute function set_photo_url_trigger();


-- При добавлении записи hero_profile поле website_url заполняется на основе nickname героя
create or replace function set_website_url_trigger()
    returns trigger as $$
begin
    new.website_url := concat('http://localhost:8888/media/', lower(new.nickname), '.com');
    return new;
end $$ language plpgsql;

create trigger set_website_url
    before insert on hero_profile for each row
    execute function set_website_url_trigger();