from django.db import models
from django.contrib.auth.models import User
from PairWise.models.courses import CourseSection


class Enrolment(models.Model):
    student_id = models.ForeignKey(User, on_delete=models.CASCADE)
    course_id = models.ForeignKey(CourseSection, on_delete=models.CASCADE)


class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    section_id = models.ForeignKey(CourseSection, on_delete=models.DO_NOTHING)
    leader = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    members = models.ManyToManyField(User)
    capacity = models.IntegerField()
    size = models.IntegerField()

    def get_members(self):
        members = list(self.members.all())
        members.append(self.leader)
        return members
