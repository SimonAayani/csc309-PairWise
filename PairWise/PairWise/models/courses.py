from django.db import models


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_code = models.CharField(max_length=10)
    name = models.CharField(max_length=255)


class TimeSection(models.Model):
    time_id = models.AutoField(primary_key=True)
    day = models.CharField(max_length=2)
    start_time = models.TimeField()
    end_time = models.TimeField()


class CourseTerm(models.Model):
    term_id = models.AutoField(primary_key=True)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    times = models.ManyToManyField(TimeSection)
    TERM_OPTIONS = (
        ('F', 'Fall'),
        ('S', 'Winter'),
        ('SF', 'Summer I'),
        ('SS', 'Summer II')
    )
    term = models.CharField(max_length=2, choices=TERM_OPTIONS)


class CourseSection(models.Model):
    section_id = models.AutoField(primary_key=True)
    term_id = models.ForeignKey(CourseTerm, on_delete=models.CASCADE)
    section_name = models.CharField(max_length=10)
