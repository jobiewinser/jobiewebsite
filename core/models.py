from django.db import models
from django.conf import settings

class TechnologyType(models.Model):
    name = models.CharField(null = True, max_length = 225, blank=True) # isams user code

class Language(models.Model):
    name = models.CharField(null = True, max_length = 225, blank=True) # isams user code

class Technology(models.Model):
    name = models.CharField(null = True, max_length = 225, blank=True) # isams user code
    type = models.ManyToManyField(TechnologyType)
    language = models.ManyToManyField(Language)

    