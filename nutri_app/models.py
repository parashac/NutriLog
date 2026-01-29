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

class DailyGoal(models.Model):
    user = models.ForeignKey(Userprofile, on_delete=models.CASCADE)
    calorie_target = models.FloatField()

    def __str__(self):
        return f"{self.user.user.username} - {self.calorie_target} kcal"

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    calories_per100g = models.FloatField(max_length=20)

    def __str__(self):
        return self.name

class Meal(models.Model):
    MEAL_TYPE= [
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
        ('Snack', 'Snack')
    ]

    user = models.ForeignKey(Userprofile, on_delete=models.CASCADE)
    meal_type = models.CharField(max_length=10, choices=MEAL_TYPE)
    date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_meal_type_display()} - {self.user.user.username}"


class FoodLog(models.Model):
    user = models.ForeignKey(Userprofile, on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.SET_NULL, null=True, blank=True)

    quantity_grams = models.FloatField()
    calories = models.FloatField(editable=False)

    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.calories = (self.food_item.calories_per100g * self.quantity_grams) / 100
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.food_item.name} - {self.calories:.2f} kcal(intake)"

class Exercise(models.Model):

    CATEGORY = [
        ('Cardio', 'Cardio'),
        ('Strength', 'Strength'),
        ('Flexibility', 'Flexibility'),
    ]

    name = models.CharField(max_length=100)
    met_value = models.FloatField()
    category = models.CharField(max_length=20, choices=CATEGORY)

    def __str__(self):
        return self.name

class ExerciseLog(models.Model):
    user = models.ForeignKey(Userprofile, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    duration_minutes = models.PositiveIntegerField()
    calories_burned = models.FloatField(editable=False)

    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        weight = self.user.weight
        self.calories_burned = (self.exercise.met_value * weight * self.duration_minutes) / 60
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.exercise.name} - {self.calories_burned:.2f} kcal(burned)"

