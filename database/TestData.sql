-- town --
INSERT INTO town VALUES (DEFAULT, 'A');
INSERT INTO town VALUES (DEFAULT, 'B');
INSERT INTO town VALUES (DEFAULT, 'C');
INSERT INTO town VALUES (DEFAULT, 'D');
INSERT INTO town VALUES (DEFAULT, 'E');
INSERT INTO town VALUES (DEFAULT, 'F');
INSERT INTO town VALUES (DEFAULT, 'G');
INSERT INTO town VALUES (DEFAULT, 'H');
INSERT INTO town VALUES (DEFAULT, 'I');
INSERT INTO town VALUES (DEFAULT, 'J');
INSERT INTO town VALUES (DEFAULT, 'K');
INSERT INTO town VALUES (DEFAULT, 'L');
INSERT INTO town VALUES (DEFAULT, 'M');
INSERT INTO town VALUES (DEFAULT, 'N');
INSERT INTO town VALUES (DEFAULT, 'O');
INSERT INTO town VALUES (DEFAULT, 'P');
INSERT INTO town VALUES (DEFAULT, 'Q');
INSERT INTO town VALUES (DEFAULT, 'R');
INSERT INTO town VALUES (DEFAULT, 'S');
INSERT INTO town VALUES (DEFAULT, 'T');
INSERT INTO town VALUES (DEFAULT, 'U');
INSERT INTO town VALUES (DEFAULT, 'V');
INSERT INTO town VALUES (DEFAULT, 'W');
INSERT INTO town VALUES (DEFAULT, 'X');
INSERT INTO town VALUES (DEFAULT, 'Y');
INSERT INTO town VALUES (DEFAULT, 'Z');

-- person --
INSERT INTO person VALUES (DEFAULT, 'Saitama', 26, NULL, NULL, NULL);
INSERT INTO person VALUES (DEFAULT, 'Director', 1, NULL, NULL, NULL);
INSERT INTO person VALUES (DEFAULT, 'Aomi', 3, NULL, NULL, NULL);
INSERT INTO person VALUES (DEFAULT, 'Beng', 6, NULL, NULL, NULL);
INSERT INTO person VALUES (DEFAULT, 'Sonic', 9, NULL, NULL, NULL);

-- dojo --
INSERT INTO dojo VALUES (DEFAULT, 'Claw', 4);

-- goverment_profile --
INSERT INTO goverment_profile VALUES (DEFAULT, 2, 'director', '2021-01-01');
INSERT INTO goverment_profile VALUES (DEFAULT, 3, 'journalist', '2021-01-01');

-- permission --
INSERT INTO permission VALUES (DEFAULT, 'может все', '2021-01-01', DEFAULT);
INSERT INTO permission VALUES (DEFAULT, 'проводить турниры', '2021-01-01', DEFAULT);
INSERT INTO permission VALUES (DEFAULT, 'писать логи', '2021-01-01', DEFAULT);
INSERT INTO permission VALUES (DEFAULT, 'проводить экзамен', '2021-01-01', DEFAULT);

-- permission_goverment_profile --
INSERT INTO permission_goverment_profile VALUES (1, 1);
INSERT INTO permission_goverment_profile VALUES (2, 2);
INSERT INTO permission_goverment_profile VALUES (3, 2);
INSERT INTO permission_goverment_profile VALUES (4, 2);

-- exam --
INSERT INTO exam VALUES (DEFAULT, 2, '2021-01-01', NULL, NULL);

-- exam_auth --
INSERT INTO exam_auth VALUES (DEFAULT, 1, 1, '2021-01-01', NULL, NULL);

-- exam_result --
INSERT INTO exam_result VALUES (DEFAULT, 1, 'phys', 100, 2);
INSERT INTO exam_result VALUES (DEFAULT, 1, 'intelligent', 71, 2);

-- exam_result --
INSERT INTO hero_profile VALUES (DEFAULT, 1, 1, 'bald', '2021-01-01', NULL, FALSE, NULL, 'aboba');
INSERT INTO hero_profile VALUES (DEFAULT, 4, NULL, 'silver claw', '2021-01-01', NULL, TRUE, NULL, 'aboba');

-- blacklist --
INSERT INTO blacklist VALUES (DEFAULT, 5, 'неадекват', '2021-01-01');

-- create menace from blacklist --
CALL PROCEDURE menaceFromBlacklist('overpowered sonic', 1, 'Еще больше неадекват', 3);
