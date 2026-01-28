from django.db import models
from django.contrib.auth.models import User

class Userprofile(models.Model):

    GENDER= [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER)
    height = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class FoodItem(models.Model):
    name_1 = models.CharField(max_length=100)
    # calories_per_100g = models.FloatField()

    def __str__(self):
        return self.name_1

class Meal(models.Model):
    MEAL_TYPE= [
        ('B', 'Breakfast'),
        ('L', 'Lunch'),
        ('D', 'Dinner'),
        ('S', 'Snack')
    ]

    user = models.ForeignKey(Userprofile, on_delete=models.CASCADE)
    meal_type = models.CharField(max_length=1, choices=MEAL_TYPE)
    date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_meal_type_display()} - {self.user.username}"


class FoodLog(models.Model):
    user = models.ForeignKey(Userprofile, on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.SET_NULL, null=True, blank=True)

    quantity_grams = models.FloatField()
    calories = models.FloatField()

    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.food_item.name} - {self.user.username}"

class Exercise(models.Model):

    CATEGORY = [
        ('C', 'Cardio'),
        ('S', 'Strength'),
        ('F', 'Flexibility'),
    ]

    name = models.CharField(max_length=100)
    met_value = models.FloatField()
    category = models.CharField(max_length=1, choices=CATEGORY)

    def __str__(self):
        return self.name

class ExerciseLog(models.Model):
    user = models.ForeignKey(Userprofile, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    duration_minutes = models.PositiveIntegerField()
    calories_burned = models.FloatField()

    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.exercise.name} - {self.user.username}"

