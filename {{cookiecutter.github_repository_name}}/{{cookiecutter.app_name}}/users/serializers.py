# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
                'id', 'username', 'auth_token', 'email', 'first_name', 'last_name',
                'is_active', 'is_staff', 'is_superuser', 'date_joined',
        )
        read_only_fields = ('username', 'auth_token', 'date_joined',)


class CreateUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        # call create_user on user object. Without this
        # the password will be stored in plain text.
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = (
                'id', 'username', 'password', 'auth_token', 'email', 'first_name', 'last_name',
                'is_active', 'date_joined',
        )
        read_only_fields = ('auth_token',)
        write_only_fields = ('password',)



