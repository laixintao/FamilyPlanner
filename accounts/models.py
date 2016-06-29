from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

class Family(models.Model):
    family_name = models.CharField('Family Name',max_length=128,blank=True)

    def __unicode__(self):
        return self.family_name

class User(AbstractUser):
    age = models.IntegerField('Age',blank=True)
    gender = models.BooleanField('Gender',blank=True) # True=Female;False=Male
    family_name = models.ForeignKey(Family,blank=True,related_name='family_member')
    role = models.BooleanField('Role',blank=True,default=True)

    def __unicode__(self):
        return self.username + " " + self.family_name.family_name