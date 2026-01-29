from django.shortcuts import render
from django.utils import timezone
from django.db import models
from nutri_app.models import ExerciseLog


# Create your views here.
def Dashboard(request):
    today = timezone.now().date()
    goal= DailyGoal.objects.get()
    target = goal.calorie_target

    total_burn = ExerciseLog.objects.filter(date = today).aggregate(total = models.Sum('calories_burned'))
    remaining = target-total_burn

    context["daily_target"] =
    context["total_burn"] =
    context["remaining"] =

    return render(request, 'home/dashboard.html', context)