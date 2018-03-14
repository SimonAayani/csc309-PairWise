from django.db import models


class DataTag(models.Model):
    id = models.AutoField(primary_key=True)
    tag_text = models.CharField(max_length=80)


class SkillTag(DataTag):
    pass


class LanguageTag(SkillTag):
    pass


class ConceptTag(SkillTag):
    pass


class FrameworkTag(SkillTag):
    pass


class LocationTag(DataTag):
    pass
