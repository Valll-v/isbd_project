create index idx_rank on ranking using hash(rank);
create index idx_raiting on ranking using btree(raiting);
create index idx_fight_style on tournament_auth using hash(style);
create index idx_exam_type on exam_result using hash(type);
create index idx_result_points on exam_result using btree(result);
