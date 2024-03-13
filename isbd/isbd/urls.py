"""
URL configuration for isbd project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index),
    path("persons", views.PersonsView.as_view(), name="persons-view"),
    path("heroes", views.HeroesView.as_view(), name="heroes-view"),
    path("menaces", views.MenacesView.as_view(), name="menaces-view"),
    path("tournaments", views.TournamentsView.as_view(), name="tournaments-view"),
    path("exams/<int:exam_id>", views.TargetExamView.as_view(), name="auth-target-view"),
    path("exams", views.ExamsView.as_view(), name="exams-view"),
    path("create_exam", views.CreateExamView.as_view(), name="create-exam-view"),
    path("exam_auths/<int:exam_id>", views.ExamAuthsView.as_view(), name="exam-auths-view"),
    path("exam_results/<int:auth_id>", views.ExamResultsView.as_view(), name="exam-results-view"),
    path("exam_register", views.ExamRegisterView.as_view(), name="exam-register-view"),
    path("make_hero", views.CreateHeroView.as_view(), name="make-hero-view"),
    path("heroes/<int:hero_id>", views.target_hero, name="target-hero-view"),
    path("create_result", views.CreateResultView.as_view(), name="create-result-view"),
    path("update_rank", views.UpdateRankView.as_view(), name="update-rank-view"),
    path("upgrade_rank/<int:hero_id>", views.upgrade_hero_rank),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
