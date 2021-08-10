#!/usr/bin/env python3

from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/charactersheet/(?P<id>[a-zA-Z]+ [a-zA-Z]+)/$', consumers.CharaktersheetConsumer.as_asgi()),
]
