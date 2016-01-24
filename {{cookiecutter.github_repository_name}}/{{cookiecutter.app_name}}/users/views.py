# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework.decorators import detail_route, list_route

from .permissions import IsOwnerOrReadOnly, IsAdminOrIsSelf
from .serializers import CreateUserSerializer, UserSerializer
from .models import User


class UserViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Creates, Updates, retrives and delete User accounts
    """
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    filter_fields = ('username', 'email', 'first_name', 'last_name', 'is_staff',
                     'is_superuser', 'is_active',)

    def list(self, request, *args, **kwargs):
        self.permission_classes = (IsAuthenticated,)
        query = self.request.query_params.get('with_deleted', None)
        if query is not None:
            self.queryset = User.objects.all()
        return super(UserViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, pk=None):
        """
        If provided 'pk' is "me" then return the current user.
        """
        if request.user and pk == 'me':
            return Response(UserSerializer(request.user).data)
        return super(UserViewSet, self).retrieve(request, pk)

    def create(self, request, *args, **kwargs):
        self.serializer_class = CreateUserSerializer
        self.permission_classes = (IsAuthenticated,)
        return super(UserViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        self.permission_classes = (IsAdminOrIsSelf,)
        return super(UserViewSet, self).update(request, *args, **kwargs)

    def destroy(self, request, pk=None):
        self.permission_classes = (IsAdminOrIsSelf,)
        user = self.get_object()
        self.perform_destroy(user)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

    @detail_route(methods=['post'], permission_classes=[IsAdminOrIsSelf,])
    def reset_password(self, request, pk=None):
        user = self.get_object()
        new_password = request.data.get('password', None)
        password_confirm = request.data.get('password_confirm', None)

        if new_password and password_confirm and new_password == password_confirm:
            user.set_password(new_password)
            user.save()
            return Response({"message" : "ok"}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"error" : "the passwords do not match"},
                            status=status.HTTP_400_BAD_REQUEST)



"""
-------------------------------------------------------------------------
    Rather than writing your own viewsets, you'll often want to use
    the existing base classes that provide a default set of behavior.
-------------------------------------------------------------------------
Example:

class UserViewSet(viewsets.ModelViewSet):
    #A viewset for viewing and editing user instances.

    serializer_class = UserSerializer
    queryset = User.objects.all()
"""

