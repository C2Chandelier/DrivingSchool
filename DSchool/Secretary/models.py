from django.db import models
from Instructor.models import Instructor
from Student.models import Student

class Secretary(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    def __str__(self):
        return self.username

class Planning(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    place = models.CharField(max_length=200)
    def __str__(self):
        return self.student.username + " " + self.instructor.username + " " + str(self.date) + " " + self.place


# Create your models here.
