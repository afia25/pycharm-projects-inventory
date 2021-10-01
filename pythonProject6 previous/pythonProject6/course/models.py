from django.db import models
from Teacher.models import Teacher


class Course(models.Model):
    crs_Title= models.TextField()
    crs_code = models.CharField(max_length=10)
    semester = models.CharField(max_length=10)
    instructor = models.ForeignKey(Teacher,null=True, on_delete=models.SET_NULL)

class Semester(models.Model):
    name= models.CharField(max_length=10)
    session = models.CharField(max_length=20)
