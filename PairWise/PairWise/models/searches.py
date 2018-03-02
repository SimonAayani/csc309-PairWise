from django.db import models
from PairWise.models.users import User
from PairWise.models.courses import CourseSection


class Searching(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    course_id = models.ForeignKey(CourseSection, on_delete=models.CASCADE)
    active_search = models.BooleanField()


class Results(models.Model):
    searcher = models.ForeignKey(User, on_delete=models.CASCADE)
    result = models.ForeignKey(User, related_name='found_id', on_delete=models.CASCADE)