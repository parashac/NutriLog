from django.urls import path
from nutri_app import views

urlpatterns = [
    path("", views.Dashboard.as_view(),name = "dashboard"),

]