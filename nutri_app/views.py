from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from django.db import models
from nutri_app.models import ExerciseLog, DailyGoal, Exercise


# Create your views here.
def DashboardView(request):
    today = timezone.now().date()
    goal= DailyGoal.objects.get()
    target = goal.calorie_target

    total_burn =( ExerciseLog.objects.filter(date = today).aggregate(total = models.Sum('calories_burned'))['total'] or 0 )
    remaining_cal = max(target-total_burn, 0)

    today_exercise = ExerciseLog.objects.filter(date=today)
    suggest_exercises = Exercise.objects.all()[:5]

    start_date = today -timedelta(days=6)
    weekly_data = (
        ExerciseLog.objects
        .filter(date__range=[start_date, today])
        .values('date')
        .annotate(total=models.Sum('calories_burned'))
        .order_by('date')
    )

    context = {
        "daily_target": target,
        "burned_today": total_burn,
        "remaining": remaining_cal,
        "today_exercises": today_exercise,
        "weekly_data": weekly_data,
        "suggested_exercises": suggest_exercises,
    }

    return render(request, "home/dashboard.html", context)
