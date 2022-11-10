from email.policy import default
from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Department(models.Model):
    dept_name = models.CharField(max_length=100)

    def __str__(self):
        return self.dept_name


class Project(models.Model):
    project_name = models.CharField(max_length=100)
    dept_name = models.ForeignKey(Department, on_delete=models.CASCADE)
    min_student = models.IntegerField()
    max_student = models.IntegerField()
    date_project = models.DateTimeField(default=timezone.now)
    author_project = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.project_name