# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import


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
