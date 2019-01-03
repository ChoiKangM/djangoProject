from django.db import models

class Post(models.Model):
    postname = models.CharField(max_length=50)
    contents = models.TextField()
