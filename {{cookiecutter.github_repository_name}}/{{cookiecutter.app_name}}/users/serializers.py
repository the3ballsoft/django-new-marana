# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'auth_token', 'email', 'first_name', 'last_name',
                  'is_active', 'is_staff', 'is_superuser', 'date_joined',)
        read_only_fields = ('username', 'auth_token', 'date_joined',)


class CreateUserSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(default=True)

    def create(self, validated_data):
        # call create_user on user object. Without this
        # the password will be stored in plain text.
        # user = User.objects.create_user(**validated_data)
        user = User.objects.create(
                 username=validated_data['username'],
                 email=validated_data['email'],
                 first_name=validated_data['first_name'],
                 last_name=validated_data['last_name'],
                 is_superuser=validated_data['is_superuser'],
                 is_staff=validated_data['is_staff']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'auth_token', 'email', 'first_name', 'last_name',
                  'is_active', 'is_staff', 'is_superuser', 'date_joined',)
        read_only_fields = ('auth_token',)
        write_only_fields = ('password',)



