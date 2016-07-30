from __future__ import unicode_literals
from django.conf import settings
from django.db import models


# Create your models here.
class Goal(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)


class Task(models.Model):
    name = models.CharField(max_length=250)
    completed = models.BooleanField(default=False)
    goal = models.ForeignKey(Goal, related_name="tasks", blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)

