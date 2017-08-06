# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from home_page.models import *

# Create your models here.

class comment(models.Model):

    user = models.ForeignKey(User,blank=True,null=True)
    title=models.CharField(max_length=30)
    comment_box=models.TextField()
    city=models.ForeignKey(Cities,blank=True,null=True)
    date_created = models.DateTimeField(auto_now=True,blank=True,null=True)

    def __unicode__(self):
        return self.title
