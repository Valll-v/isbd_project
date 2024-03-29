# Generated by Django 4.2.9 on 2024-02-28 18:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Action",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("hero_id", models.IntegerField()),
                ("responsible_id", models.IntegerField()),
                (
                    "description",
                    models.CharField(default=None, max_length=100, null=True),
                ),
                ("money", models.IntegerField()),
                ("hero_fight_id", models.IntegerField(null=True)),
            ],
            options={
                "db_table": "action",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Blacklist",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("person_id", models.IntegerField()),
                ("reason", models.CharField(max_length=100)),
                ("auth_date", models.DateTimeField()),
            ],
            options={
                "db_table": "blacklist",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Dojo",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=32, unique=True)),
                ("leader_id", models.IntegerField()),
            ],
            options={
                "db_table": "dojo",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Exam",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("responsible_id", models.IntegerField()),
                ("exam_date", models.DateTimeField()),
                ("cancel_date", models.DateTimeField(null=True)),
                ("cancel_reason", models.CharField(max_length=100, null=True)),
            ],
            options={
                "db_table": "exam",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="ExamAuth",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("person_id", models.IntegerField()),
                ("exam_id", models.IntegerField()),
                ("auth_date", models.DateTimeField()),
                ("cancel_date", models.DateTimeField(null=True)),
                ("cancel_reason", models.CharField(max_length=100, null=True)),
            ],
            options={
                "db_table": "exam_auth",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="ExamResult",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("auth_id", models.IntegerField()),
                (
                    "type",
                    models.CharField(
                        choices=[("phys", "Phys"), ("intelligent", "Intelligent")],
                        max_length=16,
                    ),
                ),
                ("result", models.IntegerField()),
                ("inspector_id", models.IntegerField()),
            ],
            options={
                "db_table": "exam_result",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="FightRecord",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("responsible_id", models.IntegerField()),
                ("hero_fight_id", models.IntegerField()),
                ("info", models.CharField(default=None, max_length=100, null=True)),
                ("creation_date", models.DateTimeField()),
            ],
            options={
                "db_table": "fight_record",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="GovermentProfile",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("person_id", models.IntegerField()),
                ("post", models.CharField(max_length=32)),
                ("start_date", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "db_table": "goverment_profile",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="HeroFight",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("menace_id", models.IntegerField()),
                ("hero_id", models.IntegerField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("announced", "Announced"),
                            ("progress", "Progress"),
                            ("win", "Win"),
                            ("lost", "Lost"),
                        ],
                        max_length=50,
                    ),
                ),
            ],
            options={
                "db_table": "hero_fight",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="HeroProfile",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("person_id", models.IntegerField(null=True, unique=True)),
                ("exam_auth_id", models.IntegerField(null=True)),
                ("nickname", models.CharField(max_length=30, unique=True)),
                ("auth_date", models.DateTimeField()),
                ("edit_date", models.DateTimeField(null=True)),
                ("without_exam", models.BooleanField(default=False)),
                ("extra_information", models.CharField(max_length=1024, null=True)),
                (
                    "website_url",
                    models.CharField(max_length=2083, null=True, unique=True),
                ),
            ],
            options={
                "db_table": "hero_profile",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Menace",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=20)),
                (
                    "description",
                    models.CharField(default=None, max_length=100, null=True),
                ),
                (
                    "level",
                    models.CharField(
                        choices=[
                            ("tiger", "Tiger"),
                            ("demon", "Demon"),
                            ("dragon", "Dragon"),
                            ("god", "God"),
                        ],
                        max_length=50,
                    ),
                ),
                ("view_date", models.DateTimeField()),
                ("view_town_id", models.IntegerField()),
                ("current_town_id", models.IntegerField(null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("death", "Death"),
                            ("alive", "Alive"),
                            ("hidden", "Hidden"),
                        ],
                        max_length=50,
                    ),
                ),
                ("from_blacklist", models.BooleanField(default=False)),
                ("blacklist_id", models.IntegerField(null=True)),
            ],
            options={
                "db_table": "menace",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="MenaceRecord",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("responsible_id", models.IntegerField()),
                ("menace_id", models.IntegerField()),
                ("info", models.CharField(max_length=512)),
                ("creation_date", models.DateTimeField()),
            ],
            options={
                "db_table": "menace_record",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Permission",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("special", models.CharField(max_length=64)),
                ("description", models.CharField(max_length=32)),
                ("creation_date", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "db_table": "permission",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="PermissionGovermentProfile",
            fields=[
                (
                    "permission_id",
                    models.IntegerField(primary_key=True, serialize=False),
                ),
                ("goverment_employee_id", models.IntegerField(unique=True)),
            ],
            options={
                "db_table": "permission_goverment_profile",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Person",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "fullname",
                    models.CharField(
                        max_length=32,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^[a-zA-Z0-9]*$",
                                code="invalid_fullname",
                                message="fullname must be Alphanumeric",
                            )
                        ],
                    ),
                ),
                ("town_id", models.IntegerField()),
                ("photo_url", models.CharField(blank=True, max_length=2083, null=True)),
                ("death_date", models.DateTimeField(blank=True, null=True)),
                ("dojo_id", models.IntegerField(blank=True, null=True)),
            ],
            options={
                "db_table": "person",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Ranking",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("hero_id", models.IntegerField()),
                ("rank", models.CharField(max_length=1)),
                ("raiting", models.IntegerField(default=None, null=True)),
                ("creation_date", models.DateTimeField()),
                ("edit_date", models.DateTimeField(null=True)),
                ("actual", models.BooleanField(default=True)),
            ],
            options={
                "db_table": "ranking",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="RankRecord",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("person_id", models.IntegerField()),
                ("auth_id", models.IntegerField()),
                (
                    "description",
                    models.CharField(default=None, max_length=100, null=True),
                ),
                ("mark", models.IntegerField()),
            ],
            options={
                "db_table": "rank_record",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Tournament",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("date", models.DateTimeField()),
                (
                    "description",
                    models.CharField(default=None, max_length=100, null=True),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("announced", "Announced"),
                            ("progress", "Progress"),
                            ("finished", "Finished"),
                            ("canceled", "Canceled"),
                        ],
                        max_length=50,
                    ),
                ),
                ("responsible_id", models.IntegerField()),
            ],
            options={
                "db_table": "tournament",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="TournamentAuth",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("person_id", models.IntegerField(null=True, unique=True)),
                ("tournament_id", models.IntegerField()),
                ("style", models.CharField(max_length=32)),
                ("cancel_date", models.DateTimeField(default=None, null=True)),
                (
                    "cancel_reason",
                    models.CharField(default=None, max_length=100, null=True),
                ),
            ],
            options={
                "db_table": "tournament_auth",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="TournamentFight",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("left_id", models.IntegerField()),
                ("right_id", models.IntegerField()),
                (
                    "result",
                    models.CharField(
                        choices=[("w1", "W1"), ("w2", "W2")], max_length=50
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("announced", "Announced"),
                            ("progress", "Progress"),
                            ("finished", "Finished"),
                        ],
                        max_length=50,
                    ),
                ),
            ],
            options={
                "db_table": "tournament_fight",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="TournamentFightRecord",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("responsible_id", models.IntegerField()),
                ("fight_id", models.IntegerField()),
                ("info", models.CharField(max_length=100)),
                ("creation_date", models.DateTimeField()),
            ],
            options={
                "db_table": "tournament_fight_record",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Town",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("code", models.CharField(max_length=1)),
            ],
            options={
                "db_table": "town",
                "managed": False,
            },
        ),
    ]
