from django.db import models


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_code = models.CharField(max_length=10)
    name = models.CharField(max_length=255)


class Term(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.PositiveSmallIntegerField()
    TERM_OPTIONS = (
        ('F', 'Fall'),
        ('S', 'Winter'),
        ('Y', 'Year-Long'),
        ('SF', 'Summer I'),
        ('SS', 'Summer II'),
        ('SY', 'Summer-Long')
    )
    term = models.CharField(max_length=2, choices=TERM_OPTIONS)


class CourseOffering(models.Model):
    id = models.AutoField(primary_key=True)
    term = models.ForeignKey(Term, on_delete=models.DO_NOTHING)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class TimeSection(models.Model):
    time_id = models.AutoField(primary_key=True)
    DAY_OPTIONS = (
        ('M', 'Monday'),
        ('T', 'Tuesday'),
        ('W', 'Wednesday'),
        ('R', 'Thursday'),
        ('F', 'Friday'),
        ('A', 'Saturday'),
        ('S', 'Sunday'),
    )
    day = models.CharField(max_length=1, choices=DAY_OPTIONS)
    start_time = models.TimeField()
    end_time = models.TimeField()


class CourseSection(models.Model):
    section_id = models.AutoField(primary_key=True)
    offering = models.ForeignKey(CourseOffering, on_delete=models.CASCADE)
    section_name = models.CharField(max_length=10)
    times = models.ManyToManyField(TimeSection)
