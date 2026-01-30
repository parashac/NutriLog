from django.urls import path
from nutri_app import views

urlpatterns = [
    path("", views.DashboardView,name="dashboard"),
    path("food-log/", views.FoodLogList, name="food-log"),
    path("food-log/add/", views.AddFood, name="add-food-log"),
    path("food-log/edit/<int:pk>", views.EditFood, name="edit-food-log"),
    path("food-log/delete/<int:pk>", views.DeleteFood, name="delete-food-log"),
    # path("exercise-log/", views.ExerciseLogView, name="exercise-log"),

]