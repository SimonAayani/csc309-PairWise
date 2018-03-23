from django.db import models
from django.contrib.auth.models import User
from PairWise_Server.models.courses import CourseOffering, Course
from PairWise_Server.models.data_tags import SkillTag, LocationTag


class Profile(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    courses = models.ManyToManyField(Course)
    location = models.ForeignKey(LocationTag, on_delete=models.CASCADE)
    skills = models.ManyToManyField(SkillTag)
    bio = models.TextField()
    pic = models.ImageField(upload_to='images/profiles/')


class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    offering = models.ForeignKey(CourseOffering, on_delete=models.DO_NOTHING)
    members = models.ManyToManyField(User)
    capacity = models.IntegerField()
    size = models.IntegerField()
