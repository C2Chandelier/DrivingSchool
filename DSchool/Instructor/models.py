from django.db import models

class Instructor(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    name = models.CharField(max_length=200,default="")
    lastname = models.CharField(max_length=200,default="")
    def __str__(self):
        return self.username
