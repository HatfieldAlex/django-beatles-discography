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
