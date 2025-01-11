from django.db import models

# Create your models here.
from django.db import models

class Movie(models.Model):
    
    title = models.CharField(max_length=30, null=False)
    genere = models.CharField(max_length=30, null=False)
    director_name = models.CharField(max_length=100)
    year = models.DateField()
    synopsis = models.TextField()

    def __str__(self):
        return self.title