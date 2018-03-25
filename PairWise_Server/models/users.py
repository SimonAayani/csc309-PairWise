from django.db import models
from django.contrib.auth.models import User
from PairWise_Server.models.courses import Course
from PairWise_Server.models.data_tags import SkillTag, LocationTag


class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course)
    location = models.ForeignKey(LocationTag, on_delete=models.CASCADE)
    skills = models.ManyToManyField(SkillTag)
    bio = models.TextField()
    pic = models.ImageField(upload_to='images/profiles/')
