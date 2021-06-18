from django.db import models

# Create your models here.


class MarkerModel(models.Model):

    title = models.CharField(max_length=100)
    tag = models.CharField(max_length=20)
    memo = models.TextField()
    lat = models.CharField(max_length=30)
    lng = models.CharField(max_length=30)

    def __str__(self):
        return self.title
