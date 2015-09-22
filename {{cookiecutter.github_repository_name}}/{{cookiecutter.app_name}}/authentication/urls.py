# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import include, url
from rest_framework.authtoken import views


urlpatterns = [
    # Token authentication
    url(r'^api-token-auth/', views.obtain_auth_token),
    # browsable API
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
