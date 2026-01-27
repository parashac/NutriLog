from django.db import models

# Create your models here.
class Fit:
    age = models.IntegerField(max_length=2)
    height = models.IntegerField(max_length=10)
    weight = models.IntegerField(max_length=10)


    def __str__(self):
        return self.age
