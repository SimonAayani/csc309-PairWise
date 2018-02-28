from django.db import models
from django.db.models.manager import BaseManager
from PairWise.models.courses import CourseSection


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    pass_salt = models.CharField(max_length=16)
    pass_hash = models.CharField(max_length=32)
    users = BaseManager()


class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    course_id = models.ForeignKey(CourseSection, on_delete=models.DO_NOTHING)
    members = models.ManyToManyField(User)
    capacity = models.IntegerField()
    size = models.IntegerField()