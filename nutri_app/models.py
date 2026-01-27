from django.db import models

# Create your models here.
class Fit(models.Model):
    user = models.OneToOneField
    age = models.IntegerField(max_length=2)
    gender = models.CharField(max_length=10)
    height = models.IntegerField(max_length=10)
    weight = models.IntegerField(max_length=10)
    food = models.CharField(max_length=100)
    meal =  models.CharField(max_length=100)
    created_at = models.TimeField(auto_now=True)
    updated_at = models.TimeField(auto_now=True)

    def __init__(self):
        return self.age
