from django.db import models
from PairWise.models.courses import CourseOffering, Course
from django.contrib.auth.models import User


class Notification(models.Model):
    id = models.AutoField(primary_key=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='receiver', on_delete=models.CASCADE)
    category = models.ForeignKey(CourseOffering, on_delete=models.CASCADE)
    text = models.TextField()
    is_invite = models.BooleanField()


class NewNotification(Notification):
    pass

