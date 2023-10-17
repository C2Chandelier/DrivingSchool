import datetime
from django.contrib import admin
from django.db import models
from django.utils import timezone


class Student(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    h_total = models.IntegerField(default=0)
    h_remaining = models.IntegerField(default=0)
    def __str__(self):
        return self.username
class Instructor(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    def __str__(self):
        return self.username
    
class Planning(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    place = models.CharField(max_length=200)
    hour = models.CharField(max_length=200)
    def __str__(self):
        return self.student.username + " " + self.instructor.username + " " + str(self.date) + " " + self.place + " " + self.hour


# Create your models here.
