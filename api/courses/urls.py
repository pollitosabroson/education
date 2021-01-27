# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

app_name = 'courses'
urlpatterns = [
    url(
        r'^$',
        views.CoursesListCreateViewSet.as_view(),
        name='list_create_courses'
    ),
    url(
        r'^(?P<public_id>[\w\-]+)$',
        views.CourseViewSet.as_view(),
        name='single_course'
    ),
]
