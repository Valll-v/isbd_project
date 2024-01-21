from django.db import models


class MenaceStatus(models.TextChoices):
    death = 'death'
    alive = 'alive'
    hidden = 'hidden'


class HeroFightStatus(models.TextChoices):
    announced = 'announced'
    progress = 'progress'
    win = 'win'
    lost = 'lost'


class TournamentStatus(models.TextChoices):
    announced = 'announced'
    progress = 'progress'
    finished = 'finished'
    canceled = 'canceled'


class MenaceLevel(models.TextChoices):
    tiger = 'tiger'
    demon = 'demon'
    dragon = 'dragon'
    god = 'god'


class ExamResultType(models.TextChoices):
    phys = 'phys'
    intelligent = 'intelligent'


class TournamentFightStatus(models.TextChoices):
    announced = 'announced'
    progress = 'progress'
    finished = 'finished'


class TournamentFightResult(models.TextChoices):
    w1 = 'w1'
    w2 = 'w2'


# Create your models here.
class Town(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=1)

    def __str__(self):
        return self.code

    class Meta:
        managed = False
        db_table = 'town'


class Dojo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, unique=True)
    leader_id = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'dojo'


class Person(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=32)
    town_id = models.IntegerField()
    photo_url = models.CharField(max_length=2083, null=True, blank=True)
    death_date = models.DateTimeField(null=True, blank=True)
    dojo_id = models.IntegerField()

    def __str__(self):
        return self.fullname

    class Meta:
        managed = False
        db_table = 'person'


class GovermentProfile(models.Model):
    id = models.AutoField(primary_key=True)
    person_id = models.IntegerField()
    post = models.CharField(max_length=32)
    start_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post

    class Meta:
        managed = False
        db_table = 'goverment_profile'


class Permission(models.Model):
    id = models.AutoField(primary_key=True)
    special = models.CharField(max_length=64)
    description = models.CharField(max_length=32)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description

    class Meta:
        managed = False
        db_table = 'permission'


class PermissionGovermentProfile(models.Model):
    permission_id = models.IntegerField(primary_key=True)
    goverment_employee_id = models.IntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'permission_goverment_profile'
        unique_together = ('permission_id', 'goverment_employee_id')


class Exam(models.Model):
    id = models.AutoField(primary_key=True)
    responsible_id = models.IntegerField()
    exam_date = models.DateTimeField()
    cancel_date = models.DateTimeField(null=True)
    cancel_reason = models.CharField(max_length=100, null=True)

    class Meta:
        managed = False
        db_table = 'exam'


class ExamAuth(models.Model):
    id = models.AutoField(primary_key=True)
    person_id = models.IntegerField()
    exam_id = models.IntegerField()
    auth_date = models.DateTimeField()
    cancel_date = models.DateTimeField(null=True)
    cancel_reason = models.CharField(max_length=100, null=True)

    class Meta:
        managed = False
        db_table = 'exam_auth'


class ExamResult(models.Model):
    id = models.AutoField(primary_key=True)
    auth_id = models.IntegerField()
    type = models.CharField(max_length=16, choices=ExamResultType.choices)
    result = models.IntegerField()
    inspector_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'exam_result'


class HeroProfile(models.Model):
    id = models.AutoField(primary_key=True)
    person_id = models.IntegerField(unique=True, null=True)
    exam_auth_id = models.IntegerField(null=True)
    nickname = models.CharField(max_length=30, unique=True)
    auth_date = models.DateTimeField()
    edit_date = models.DateTimeField(null=True)
    without_exam = models.BooleanField(default=False)
    extra_information = models.CharField(max_length=1024, null=True)
    website_url = models.CharField(max_length=2083, unique=True, null=True)

    class Meta:
        managed = False
        db_table = 'hero_profile'


class Ranking(models.Model):
    id = models.AutoField(primary_key=True)
    hero_id = models.IntegerField()
    rank = models.CharField(max_length=1)
    raiting = models.IntegerField(null=True, default=None)
    creation_date = models.DateTimeField()
    edit_date = models.DateTimeField(null=True)
    actual = models.BooleanField(default=True)

    class Meta:
        managed = False
        db_table = 'ranking'


class Blacklist(models.Model):
    id = models.AutoField(primary_key=True)
    person_id = models.IntegerField()
    reason = models.CharField(max_length=100)
    auth_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'blacklist'


class Menace(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100, null=True, default=None)
    level = models.CharField(max_length=50, choices=MenaceLevel.choices)
    view_date = models.DateTimeField()
    view_town_id = models.IntegerField()
    current_town_id = models.IntegerField(null=True)
    status = models.CharField(max_length=50, choices=MenaceStatus.choices)
    from_blacklist = models.BooleanField(default=False)
    blacklist_id = models.IntegerField(null=True)

    class Meta:
        managed = False
        db_table = 'menace'


class MenaceRecord(models.Model):
    id = models.AutoField(primary_key=True)
    responsible_id = models.IntegerField()
    menace_id = models.IntegerField()
    info = models.CharField(max_length=512)
    creation_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'menace_record'


class HeroFight(models.Model):
    id = models.AutoField(primary_key=True)
    menace_id = models.IntegerField()
    hero_id = models.IntegerField()
    status = models.CharField(max_length=50, choices=HeroFightStatus.choices)

    class Meta:
        managed = False
        db_table = 'hero_fight'


class FightRecord(models.Model):
    id = models.AutoField(primary_key=True)
    responsible_id = models.IntegerField()
    hero_fight_id = models.IntegerField()
    info = models.CharField(max_length=100, null=True, default=None)
    creation_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'fight_record'


class Action(models.Model):
    id = models.AutoField(primary_key=True)
    hero_id = models.IntegerField()
    responsible_id = models.IntegerField()
    description = models.CharField(max_length=100, null=True, default=None)
    money = models.IntegerField()
    hero_fight_id = models.IntegerField(null=True)

    class Meta:
        managed = False
        db_table = 'action'


class Tournament(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    description = models.CharField(max_length=100, null=True, default=None)
    status = models.CharField(max_length=50, choices=TournamentStatus.choices)
    responsible_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tournament'


class TournamentAuth(models.Model):
    id = models.AutoField(primary_key=True)
    person_id = models.IntegerField(unique=True, null=True)
    tournament_id = models.IntegerField()
    style = models.CharField(max_length=32)
    cancel_date = models.DateTimeField(null=True, default=None)
    cancel_reason = models.CharField(max_length=100, null=True, default=None)

    class Meta:
        managed = False
        db_table = 'tournament_auth'


class RankRecord(models.Model):
    id = models.AutoField(primary_key=True)
    person_id = models.IntegerField()
    auth_id = models.IntegerField()
    description = models.CharField(max_length=100, null=True, default=None)
    mark = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rank_record'


class TournamentFight(models.Model):
    id = models.AutoField(primary_key=True)
    left_id = models.IntegerField()
    right_id = models.IntegerField()
    result = models.CharField(max_length=50,
                              choices=TournamentFightResult.choices)
    status = models.CharField(max_length=50,
                              choices=TournamentFightStatus.choices)

    class Meta:
        managed = False
        db_table = 'tournament_fight'


class TournamentFightRecord(models.Model):
    id = models.AutoField(primary_key=True)
    responsible_id = models.IntegerField()
    fight_id = models.IntegerField()
    info = models.CharField(max_length=100)
    creation_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tournament_fight_record'
