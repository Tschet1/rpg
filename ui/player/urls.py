#!/usr/bin/env python3

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/get/<str:name>', views.get_person, name='get_person'),
]
