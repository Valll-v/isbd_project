ALTER TABLE person
    ADD FOREIGN KEY (town_id) REFERENCES town (id);

ALTER TABLE person
    ADD FOREIGN KEY (dojo_id) REFERENCES dojo (id);

ALTER TABLE goverment_profile
    ADD FOREIGN KEY (person_id) REFERENCES person (id);

ALTER TABLE permission_goverment_profile
    ADD FOREIGN KEY (permission_id) REFERENCES permission (id);
ALTER TABLE permission_goverment_profile
    ADD FOREIGN KEY (goverment_employee_id) REFERENCES goverment_profile (id);
ALTER TABLE exam
    ADD FOREIGN KEY (responsible_id) REFERENCES goverment_profile (id);
ALTER TABLE exam_auth
    ADD FOREIGN KEY (person_id) REFERENCES person (id);
ALTER TABLE exam_auth
    ADD FOREIGN KEY (exam_id) REFERENCES exam (id);
ALTER TABLE exam_result
    ADD FOREIGN KEY (auth_id) REFERENCES exam_auth (id);
ALTER TABLE exam_result
    ADD FOREIGN KEY (inspector_id) REFERENCES goverment_profile (id);
ALTER TABLE hero_profile
    ADD FOREIGN KEY (person_id) REFERENCES person (id);
ALTER TABLE hero_profile
    ADD FOREIGN KEY (exam_auth_id) REFERENCES exam_auth (id);
ALTER TABLE ranking
    ADD FOREIGN KEY (hero_id) REFERENCES hero_profile (id);
ALTER TABLE blacklist
    ADD FOREIGN KEY (person_id) REFERENCES person (id);
ALTER TABLE menace
    ADD FOREIGN KEY (blacklist_id) REFERENCES blacklist (id);
ALTER TABLE menace_record
    ADD FOREIGN KEY (responsible_id) REFERENCES goverment_profile (id);
ALTER TABLE menace_record
    ADD FOREIGN KEY (menace_id) REFERENCES menace (id);
ALTER TABLE hero_fight
    ADD FOREIGN KEY (menace_id) REFERENCES menace (id);
ALTER TABLE hero_fight
    ADD FOREIGN KEY (hero_id) REFERENCES hero_profile (id);
ALTER TABLE fight_record
    ADD FOREIGN KEY (responsible_id) REFERENCES goverment_profile (id);
ALTER TABLE fight_record
    ADD FOREIGN KEY (hero_fight_id) REFERENCES hero_fight (id);
ALTER TABLE action
    ADD FOREIGN KEY (hero_id) REFERENCES hero_profile (id);
ALTER TABLE action
    ADD FOREIGN KEY (responsible_id) REFERENCES goverment_profile (id);
ALTER TABLE action
    ADD FOREIGN KEY (hero_fight_id) REFERENCES hero_fight (id);
ALTER TABLE dojo
    ADD FOREIGN KEY (leader_id) REFERENCES person (id);
ALTER TABLE tournament
    ADD FOREIGN KEY (responsible_id) REFERENCES goverment_profile (id);
ALTER TABLE tournament_auth
    ADD FOREIGN KEY (person_id) REFERENCES person (id);
ALTER TABLE tournament_auth
    ADD FOREIGN KEY (tournament_id) REFERENCES tournament (id);
ALTER TABLE rank_record
    ADD FOREIGN KEY (person_id) REFERENCES person (id);
ALTER TABLE rank_record
    ADD FOREIGN KEY (auth_id) REFERENCES tournament_auth (id);
ALTER TABLE tournament_fight
    ADD FOREIGN KEY (left_id) REFERENCES tournament_auth (id);
ALTER TABLE tournament_fight
    ADD FOREIGN KEY (right_id) REFERENCES tournament_auth (id);
ALTER TABLE tournament_fight_record
    ADD FOREIGN KEY (responsible_id) REFERENCES goverment_profile (id);

ALTER TABLE tournament_fight_record
    ADD FOREIGN KEY (fight_id) REFERENCES tournament_fight (id);

