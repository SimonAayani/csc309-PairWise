from django.db import models
from PairWise.models.users import User, Group
from PairWise.models.courses import CourseOffering
from PairWise.models.data_tags import SkillTag


class SearchEntry(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(CourseOffering, on_delete=models.CASCADE)
    subhead = models.CharField(max_length=255)
    capacity = models.PositiveSmallIntegerField()
    description = models.TextField()
    desired_fields = models.ManyToManyField(SkillTag)
    active_search = models.BooleanField(default=True)


class UserSearchEntry(SearchEntry):
    host = models.ForeignKey(User, on_delete=models.CASCADE)


class GroupSearchEntry(SearchEntry):
    host = models.ForeignKey(Group, on_delete=models.CASCADE)


class SearchResultsCache(models.Model):
    searcher = models.ForeignKey(SearchEntry, on_delete=models.CASCADE)
    result = models.ForeignKey(SearchEntry, related_name='found', on_delete=models.CASCADE)