from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    auth = models.CharField(max_length=100)
    data = models.DateField()


def __str__(self):
    return self.title