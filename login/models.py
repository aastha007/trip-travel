# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class user(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

    def __unicode__(self):
        return self.username
