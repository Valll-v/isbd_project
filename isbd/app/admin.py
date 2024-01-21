from django.contrib import admin
from app.models import *


# Register your models here.
@admin.register(Dojo)
class DojoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Dojo._meta.get_fields()]


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Person._meta.get_fields()]


@admin.register(Town)
class TownAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Town._meta.get_fields()]


@admin.register(GovermentProfile)
class GovermentProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in GovermentProfile._meta.get_fields()]


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Permission._meta.get_fields()]


@admin.register(PermissionGovermentProfile)
class PermissionGovermentProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in
                    PermissionGovermentProfile._meta.get_fields()]


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = [field.name for field in
                    Exam._meta.get_fields()]


@admin.register(ExamAuth)
class ExamAuthAdmin(admin.ModelAdmin):
    list_display = [field.name for field in
                    ExamAuth._meta.get_fields()]


@admin.register(ExamResult)
class ExamResultAdmin(admin.ModelAdmin):
    list_display = [field.name for field in
                    ExamResult._meta.get_fields()]


@admin.register(HeroProfile)
class HeroProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in
                    HeroProfile._meta.get_fields()]


@admin.register(Ranking)
class RankingAdmin(admin.ModelAdmin):
    list_display = [field.name for field in
                    Ranking._meta.get_fields()]


@admin.register(Blacklist)
class BlacklistAdmin(admin.ModelAdmin):
    list_display = [field.name for field in
                    Blacklist._meta.get_fields()]


@admin.register(Menace)
class MenaceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in
                    Menace._meta.get_fields()]


@admin.register(MenaceRecord)
class MenaceRecordAdmin(admin.ModelAdmin):
    list_display = [field.name for field in
                    MenaceRecord._meta.get_fields()]


@admin.register(HeroFight)
class HeroFightAdmin(admin.ModelAdmin):
    list_display = [field.name for field in
                    HeroFight._meta.get_fields()]


@admin.register(FightRecord)
class FightRecordAdmin(admin.ModelAdmin):
    list_display = [field.name for field in
                    FightRecord._meta.get_fields()]


@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in
                    Action._meta.get_fields()]


@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in
                    Tournament._meta.get_fields()]


@admin.register(TournamentAuth)
class TournamentAuthAdmin(admin.ModelAdmin):
    list_display = [field.name for field in
                    TournamentAuth._meta.get_fields()]


@admin.register(RankRecord)
class RankRecordAdmin(admin.ModelAdmin):
    list_display = [field.name for field in
                    RankRecord._meta.get_fields()]


@admin.register(TournamentFight)
class TournamentFightAdmin(admin.ModelAdmin):
    list_display = [field.name for field in
                    TournamentFight._meta.get_fields()]


@admin.register(TournamentFightRecord)
class TournamentFightRecordAdmin(admin.ModelAdmin):
    list_display = [field.name for field in
                    TournamentFightRecord._meta.get_fields()]


