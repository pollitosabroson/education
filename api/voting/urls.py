# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

app_name = 'voting'
urlpatterns = [
    url(
        r'^$',
        views.VoteCreateViewSet.as_view(),
        name='create_vote'
    )
]
