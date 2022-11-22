# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Contact(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=50, default=None)
    email = models.EmailField(max_length=254, blank=True, null=True)
    counter_is = models.CharField(max_length=242, blank=True, null=True)
    unique_code = models.UUIDField(null=True, blank=True, unique=True)
    dob = models.DateField(default=None)

    def __str__(self):
        return self.email
