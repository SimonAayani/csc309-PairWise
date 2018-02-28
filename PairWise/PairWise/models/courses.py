from django.db import models


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_code = models.CharField(max_length=12)
    name = models.CharField(max_length=255)


class TimeSection(models.Model):
    time_id = models.AutoField(primary_key=True)
    day = models.CharField(max_length=2)
    start_time = models.TimeField()
    end_time = models.TimeField()


class CourseSection(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    section_code = models.CharField(max_length=10)
    term = models.CharField(max_length=12)
    times = models.ManyToManyField(TimeSection)