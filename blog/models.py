from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=30)
    desc = models.TextField(max_length=500)