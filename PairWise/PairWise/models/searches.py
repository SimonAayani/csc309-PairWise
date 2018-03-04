from django.db import models
from PairWise.models.users import User, Group
from PairWise.models.courses import CourseTerm
from PairWise.models.data_tags import SkillTag


class SearchEntry(models.Model):
    category = models.ForeignKey(CourseTerm, on_delete=models.CASCADE)
    subhead = models.CharField(max_length=255)
    capacity = models.PositiveSmallIntegerField()
    description = models.TextField()
    desired_fields = models.ManyToManyField(SkillTag)


class UserSearchEntry(SearchEntry):
    host = models.ForeignKey(User, on_delete=models.CASCADE)


class GroupSearchEntry(SearchEntry):
    host = models.ForeignKey(Group, on_delete=models.CASCADE)


class Search(models.Model):
    id = models.AutoField(primary_key=True)
    searcher = models.ForeignKey(SearchEntry, on_delete=models.CASCADE)
    active_search = models.BooleanField()


class SearchResultsCache(models.Model):
    searcher = models.ForeignKey(Search, on_delete=models.CASCADE)
    result = models.ForeignKey(Search, related_name='found', on_delete=models.CASCADE)