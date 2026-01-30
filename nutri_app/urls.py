from django.urls import path
from nutri_app import views

urlpatterns = [
    path("", views.DashboardView,name="dashboard"),
    # path("dashboard/", views.DashboardView().as_view(), name="dashboard")
]