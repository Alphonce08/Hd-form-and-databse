from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    email = models.CharField(max_length=30, blank=False, null=False)
    idnum = models.IntegerField(max_length=30, blank=False, null=False)


def __str__(self):
    return self.name