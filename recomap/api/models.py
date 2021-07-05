from django.db import models


class Snippet(models.Model):

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    images = models.ImageField(upload_to='', null=True)
    tag = models.CharField(max_length=20, null=True)
    memo = models.TextField(null=True)
    lat = models.CharField(max_length=30)
    lng = models.CharField(max_length=30)
    class Meta:
        ordering = ('title',)



