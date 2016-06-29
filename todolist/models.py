from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Todo(models.Model):
    user = models.ForeignKey('accounts.User',related_name='my_todo')
    family = models.ForeignKey('accounts.Family',related_name='family_todo')
    task = models.CharField('Task',max_length=300)
    deadline = models.DateTimeField('Deadline')

    def __unicode__(self):
        return self.task