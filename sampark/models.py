from __future__ import unicode_literals

from django.db import models

# Create your models here.
class contus(models.Model):
    Name = models.CharField(max_length=25)
    Email = models.EmailField(null=True,blank=True)
    Phone_No = models.IntegerField()
    Comment = models.TextField()

    def __unicode__(self):
        return self.Name

class sugus(models.Model):
    Name = models.CharField(max_length=25)
    Email = models.EmailField(null=True,blank=True)
    Country = models.CharField(max_length=30)
    Place = models.CharField(max_length=25)
    About = models.TextField()

    def __unicode__(self):
        return self.Name
