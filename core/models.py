from django.db import models
from django.db.models.deletion import SET_NULL

class HomeDevice(models.Model):
    sw_ver = models.CharField(null = True, max_length = 225, blank=True)
    hw_ver = models.CharField(null = True, max_length = 225, blank=True)
    type = models.CharField(null = True, max_length = 225, blank=True)
    hwId = models.CharField(null = True, max_length = 225, blank=True)
    fwId = models.CharField(null = True, max_length = 225, blank=True)
    oemId = models.CharField(null = True, max_length = 225, blank=True)
    dev_name = models.CharField(null = True, max_length = 225, blank=True)
    alias = models.CharField(null = True, max_length = 225, blank=True)
    updated = models.DateTimeField(auto_now=True)
    mac = models.CharField(max_length = 225, unique=True)

    def __str__(self):
        return self.dev_name

class HomePlug(HomeDevice):

    def __str__(self):
        return self.dev_name

class EnergyDayReading(models.Model):
    homeplug = models.ForeignKey(HomePlug, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    nice_date = models.CharField(null = True, max_length = 225, blank=True)
    energy_wh = models.IntegerField(null = True, blank=True)


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
    type = models.ManyToManyField(TechnologyType, null = True, blank=True)
    language = models.ManyToManyField(Language, null = True, blank=True)
    image = models.FileField(null = True, blank=True, upload_to='technology-images')
    priority = models.IntegerField(null = True, blank=True)
    htmldescription = models.CharField(null = True, max_length = 500, blank=True)

    def __str__(self):
        return self.name

    
class Project(models.Model):
    name = models.CharField(null = True, max_length = 225, blank=True)
    start = models.DateField(null=True, blank=True)
    end = models.DateField(null=True, blank=True)
    technology = models.ManyToManyField(Technology, blank=True)
    htmldescription = models.CharField(null = True, max_length = 4000, blank=True)
    shorthtmldescription = models.CharField(null = True, max_length = 1000, blank=True)
    role = models.CharField(null = True, max_length = 500, blank=True)
    teamsize = models.IntegerField(null = True, blank=True)

    def __str__(self):
        return self.name
    def get_languages(self):
        return Language.objects.filter(technology__in=self.technology.all()).distinct('pk')
    
class ProjectImage(models.Model):
    image = models.FileField(null = True, upload_to='technology-images')
    htmldescription = models.CharField(null = True, max_length = 5000, blank=True)
    project = models.ManyToManyField(Project, null=True, blank=True)
    priority = models.IntegerField(null = True, blank=True)
    show_on_demo = models.BooleanField(default=False)

    class Meta:
        ordering = ['priority']

    
