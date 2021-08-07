from django.db import models
from django.db.models.deletion import SET_NULL

class TechnologyType(models.Model):
    name = models.CharField(null = True, max_length = 225, blank=True)

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(null = True, max_length = 225, blank=True)

    def __str__(self):
        return self.name


class Technology(models.Model):
    name = models.CharField(null = True, max_length = 225, blank=True)
    type = models.ManyToManyField(TechnologyType)
    language = models.ManyToManyField(Language)
    image = models.FileField(null = True, upload_to='technology-images')
    priority = models.IntegerField(null = True, blank=True)
    htmldescription = models.IntegerField(null = True, blank=True)

    def __str__(self):
        return self.name

    
class Project(models.Model):
    name = models.CharField(null = True, max_length = 225, blank=True)
    start = models.DateField(null=True, blank=True)
    end = models.DateField(null=True, blank=True)
    technology = models.ManyToManyField(Technology)
    htmldescription = models.CharField(null = True, max_length = 4000, blank=True)
    shortdescription = models.CharField(null = True, max_length = 1000, blank=True)

    def __str__(self):
        return self.name
    
class ProjectImage(models.Model):
    image = models.FileField(null = True, upload_to='technology-images')
    htmldescription = models.CharField(null = True, max_length = 5000, blank=True)
    project = models.ForeignKey(Project, on_delete=SET_NULL, null=True)

    