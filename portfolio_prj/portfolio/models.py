from django.db import models


class About(models.Model):
    shot_description = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to="about")
    resume = models.FileField(upload_to="resume")
    

    class Meta:
        verbose_name = ("About Me")
        verbose_name_plural = ("About Me")

    def __str__(self):
        return "About"


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class RecentWork(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="work")


    def __str__(self):
        return self.title

class Client(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="work")


    def __str__(self):
        return self.title