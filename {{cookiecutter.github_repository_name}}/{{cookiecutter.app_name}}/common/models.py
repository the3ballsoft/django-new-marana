# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.encoding import python_2_unicode_compatible


class TimeStampedModel(models.Model):
    """
    Una clase abstracta que registra la fecha de creacion,
    modificacion y eliminacion del modelo
    """
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    modified = models.DateTimeField(auto_now=True, verbose_name="fecha de modificacion")
    deleted = models.BooleanField(default=False, verbose_name="eliminado")

    class Meta:
        abstract = True

class SoftDeleteManager(models.Manager):
    """ Use this manager to get objects that have a deleted field """
    def get_query_set(self):
        return super(SoftDeleteManager, self).get_query_set().filter(deleted=False)
    def all_with_deleted(self):
        return super(SoftDeleteManager, self).get_query_set()
    def deleted_set(self):
        return super(SoftDeleteManager, self).get_query_set().filter(deleted=True)
