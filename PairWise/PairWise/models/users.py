from django.db import models
from django.contrib.auth.models import User
from PairWise.models.courses import CourseTerm, Course
from PairWise.models.data_tags import SkillTag


class Profile(models.Model):
    student_id = models.ForeignKey(User, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course, null=True)
    location = models.CharField(max_length=255, null=True)
    skills = models.ManyToManyField(SkillTag)
    bio = models.TextField()
    pic = models.ImageField(null=True)


class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    section_id = models.ForeignKey(CourseTerm, on_delete=models.DO_NOTHING)
    members = models.ManyToManyField(User)
    capacity = models.IntegerField()
    size = models.IntegerField()
