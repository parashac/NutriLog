from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from datetime import timedelta
from django.db import models

from nutri_app.forms import FoodLogForm
from nutri_app.models import ExerciseLog, DailyGoal, Exercise, FoodLog
from nutri_app.models import FoodLog

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
    today_intake = (
            FoodLog.objects
            .filter(user=request.user.userprofile, date=today)
            .aggregate(total=models.Sum('calories'))['total'] or 0
    )

    context = {
        "daily_target": target,
        "burned_today": total_burn,
        "remaining": remaining_cal,
        "today_exercises": today_exercise,
        "weekly_data": weekly_data,
        "suggested_exercises": suggest_exercises,
        "today_intake": today_intake,
    }

    return render(request, "home/dashboard.html", context)

def FoodLogList(request):
    today = timezone.now().date()
    user_profile = request.user.userprofile

    today_intake = (
        FoodLog.objects
        .filter(user=user_profile, date=today)
        .aggregate(total=models.Sum('calories'))['total'] or 0
    )

    burned_today = (
        ExerciseLog.objects
        .filter(user=user_profile, date=today)
        .aggregate(total=models.Sum('calories_burned'))['total'] or 0
    )
    food_logs = FoodLog.objects.filter(
        user=user_profile
    ).order_by('-date')

    context = {
        "food_logs": food_logs,
        "today_intake": today_intake,
        "burned_today": burned_today,
    }

    return render(request, 'food log/food-list.html', context)

def AddFood(request):
    """
    Add a new food entry.
    """
    if request.method == 'POST':
        form = FoodLogForm(request.POST)
        if form.is_valid():
            food_log = form.save(commit=False)
            food_log.user = request.user.userprofile  # link to Userprofile
            food_log.save()
            return redirect('food-log')
    else:
        form = FoodLogForm()

    return render(request, 'food log/add-food.html', {
        'form': form,
        'title': 'Add Food'
    })
def EditFood(request, pk):
    """
    Edit an existing food entry.
    """
    food_item = get_object_or_404(FoodLog, id=pk, user=request.user.userprofile)

    if request.method == 'POST':
        form = FoodLogForm(request.POST, instance=food_item)
        if form.is_valid():
            form.save()
            return redirect('food-log')
    else:
        form = FoodLogForm(instance=food_item)

    return render(request, 'food log/edit-food.html', {
        'form': form,
        'title': 'Edit Food',
        'edit_item': food_item
    })
def DeleteFood(request, pk):
    """
    Delete a food entry with confirmation.
    """
    food_item = get_object_or_404(FoodLog, id=pk, user=request.user.userprofile)

    if request.method == 'POST':
        food_item.delete()
        return redirect('food-log')

    return render(request, 'food log/delete.html', {
        'food': food_item
    })