# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

app_name = 'professors'
urlpatterns = [
    url(
        r'^$',
        views.ProfessorsListCreateViewSet.as_view(),
        name='list_create_professors'
    ),
    url(
        r'^(?P<public_id>[\w\-]+)$',
        views.ProfessorViewSet.as_view(),
        name='profile_professor'
    ),
]
