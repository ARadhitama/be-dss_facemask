from django.contrib import admin
from django.urls import path, include
from api import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('dashboard/', csrf_exempt(views.DashboardView.as_view()))
]