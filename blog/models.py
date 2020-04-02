from django.db import models

# Create your models here.
# blog app model.py
class Author(models.Model):
    username = models.CharField(max_length=50 , unique=True , blank=False)
    password = models.CharField(max_length=35)
    email = models.EmailField(unique=True) #aid = models.AutoField()


class Posts(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    postDate = models.DateTimeField()
