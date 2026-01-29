from django.contrib import admin
from nutri_app.models import Userprofile, FoodItem, Meal, FoodLog, Exercise, ExerciseLog, DailyGoal

# Register your models here.
admin.site.register(Userprofile)
admin.site.register(FoodItem)
admin.site.register(Meal)
admin.site.register(FoodLog)
admin.site.register(Exercise)
admin.site.register(ExerciseLog)
admin.site.register(DailyGoal)
