from django.db import models

# Create your models here.

class Album(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    release_year = models.CharField(max_length=4)
    label = models.CharField(max_length=100)
    fun_fact = models.TextField()

    def __str__(self):
        return self.name

class Track(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='tracks')
    title = models.CharField(max_length=100)
    duration = models.DurationField()
    position = models.IntegerField()
    lead_vocals = models.CharField(max_length=100, default='Lennon and McCartney')

    def __str__(self):
        return self.title
