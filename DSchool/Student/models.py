from django.db import models

class Student(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    h_total = models.IntegerField(default=0)
    h_remaining = models.IntegerField(default=0)
    def __str__(self):
        return self.username


