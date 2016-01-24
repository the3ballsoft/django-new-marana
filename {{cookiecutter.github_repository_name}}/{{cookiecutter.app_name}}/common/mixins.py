# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from rest_framework import status
from rest_framework.response import Response


class DestroyModelMixin(object):
    """
    Destroy a model instance. support for softdelete
    """
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.deleted = True
        instance.save()

class ListModelMixin(object):
    """
    List a queryset. support for softdetele
    """
    def list(self, request, *args, **kwargs):
        query = self.request.query_params.get('with_deleted', None)
        if query is not None:
            queryset = self.filter_queryset(self.get_queryset())
        else:
            queryset = self.filter_queryset(self.get_queryset().filter(deleted=False))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
