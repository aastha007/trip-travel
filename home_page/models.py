from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

class Countries(models.Model):
    Id = models.CharField(primary_key=True,max_length=10)
    Name = models.CharField(max_length=50)
    Location = models.CharField(max_length=50)
    About = models.TextField()
    Image = models.ImageField(upload_to="Countries",blank=True,null=True)

    def __unicode__(self):
        return self.Name

    def get_absolute_url(self):
        return reverse('index')

class Cities(models.Model):
    Id = models.ForeignKey(Countries, related_name='cities')
    C_Id = models.CharField(primary_key=True,max_length=10)
    Name = models.CharField(max_length=50)
    Type = models.CharField(max_length=30)
    Best_time_to_visit = models.CharField(max_length=20)
    About = models.TextField()
    Image = models.ImageField(upload_to="Images",blank=True,null=True)
    #comment = models.ForeignKey(comment,blank=True,null=True)

    def __unicode__(self):
        return self.Name
