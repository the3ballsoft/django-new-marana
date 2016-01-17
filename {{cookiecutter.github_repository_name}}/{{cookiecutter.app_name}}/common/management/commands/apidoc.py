# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from subprocess import call



from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Generate apidocs files'

    def handle(self, *args, **options):
        call(["apidoc", "-f", ".py", "-i", "./", "-o", "templates/apidoc"])
