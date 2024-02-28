-- Создание угрозы из черного списка
CREATE PROCEDURE menaceFromBlacklist
(
 menaceNickname VARCHAR(20),
 blacklistID INTEGER,
 description VARCHAR(100),
 currentTown INTEGER
) AS
$$
 INSERT INTO menace
 VALUES
 (
  DEFAULT,
  menaceNickname,
  description,
  'tiger',
  (
   SELECT auth_date
    FROM blacklist
   WHERE id = blacklistID
   LIMIT 1
  ),
  (
   SELECT town.id
    FROM blacklist
    JOIN person ON
     blacklist.person_id = person.id
    JOIN town ON
     town.id = person.town_id
    WHERE blacklist.id = blacklistID
    LIMIT 1
  ),
  currentTown,
  'alive',
  TRUE,
  blacklistID
 );
$$
LANGUAGE SQL;

-- Проверка перед созданием профиля героя, что человек с данным id успешно прошел phys и intelligent экзамен, если
-- without_exam == true проверка не происходит, человек успешно сдал экз если по phys >= 70 и intelligent >= 70
CREATE OR REPLACE PROCEDURE checkExamToAddHeroProfile(
 person INTEGER,
 hero_nickname VARCHAR(30),
 auth_date timestamp,
 without_exam bool,
 extra_information varchar(1024)
)
LANGUAGE plpgsql
AS $$
DECLARE
    found_exam_auth_id INTEGER;
    passed_both BOOLEAN;
BEGIN
    IF without_exam THEN
        INSERT INTO hero_profile(person_id, exam_auth_id, nickname, auth_date, without_exam, extra_information)
        VALUES (person, NULL, hero_nickname, auth_date, without_exam, extra_information);
    ELSE
        -- Нахождение exam_auth_id для данного person_id
        SELECT id INTO found_exam_auth_id
        FROM exam_auth
        WHERE person_id = person;

        -- Проверка наличия двух необходимых результатов экзаменов
        SELECT (COUNT(*) = 2) INTO passed_both
        FROM exam_result
        WHERE auth_id = found_exam_auth_id AND (
              (type = 'phys' AND result >= 70)
           OR (type = 'intelligent' AND result >= 70)
        )
        GROUP BY type;

        IF passed_both THEN
            INSERT INTO hero_profile(person_id, exam_auth_id, nickname, auth_date, without_exam, extra_information)
            VALUES (person, found_exam_auth_id, hero_nickname, auth_date, without_exam, extra_information);
        ELSE
            RAISE EXCEPTION 'Не был сдан один из этапов экзамена';
        END IF;
    END IF;
END;
$$;

-- Процедура создания додзе - у человека, которого назначают лидером dojo_id принимает значение id созданного додзе
CREATE OR REPLACE PROCEDURE add_dojo_and_update_leader(
    dojo_name VARCHAR(32),
    leader_id INTEGER
)
LANGUAGE plpgsql
AS $$
DECLARE
    new_dojo_id INTEGER;
BEGIN
    -- Добавление записи в dojo
    INSERT INTO dojo(name, leader_id)
    VALUES (dojo_name, leader_id)
    RETURNING id INTO new_dojo_id;

    -- Обновление dojo_id для лидера
    UPDATE person
    SET dojo_id = new_dojo_id
    WHERE id = leader_id;
END;
$$;
