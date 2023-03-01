from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    year_of_study = models.IntegerField()
    
    def __str__(self):
        return self.name + " " + self.surname
