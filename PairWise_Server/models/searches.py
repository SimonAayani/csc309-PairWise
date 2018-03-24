from django.db import models
from PairWise_Server.models.users import User
from PairWise_Server.models.courses import CourseOffering, CourseSection
from PairWise_Server.models.data_tags import SkillTag, LocationTag


class SearchEntry(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(CourseOffering, on_delete=models.SET_NULL)
    title = models.CharField(max_length=255)
    description = models.TextField()
    capacity = models.PositiveSmallIntegerField()
    required_section = models.ForeignKey(CourseSection, on_delete=models.SET_NULL)
    active_search = models.BooleanField(default=True)


class UserSearchEntry(SearchEntry):
    host = models.ForeignKey(UserSearchData, on_delete=models.CASCADE)


class GroupSearchEntry(SearchEntry):
    members = models.ManyToManyField(UserSearchData)
    size = models.PositiveSmallIntegerField()


class UserSearchData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
    desired_skills = models.ForeignKey(SkillTag, on_delete=models.CASCADE)
    course_section = models.ForeignKey(CourseSection, on_delete=models.SET_NULL)
    location = models.ForeignKey(LocationTag, on_delete=models.SET_NULL)


class SearchResultsCache(models.Model):
    searcher = models.ForeignKey(SearchEntry, on_delete=models.CASCADE)
    result = models.ForeignKey(SearchEntry, related_name='found', on_delete=models.CASCADE)
    match_coefficient = models.PositiveSmallIntegerField()