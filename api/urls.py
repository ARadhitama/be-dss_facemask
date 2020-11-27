from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('post_pengunjung/', views.post_pengunjung),
    path('count_pengunjung/', views.get_total_pengunjung),
    path('count_pelanggaran/', views.get_total_pelanggaran),
    path('count_aman/', views.get_total_aman),
    path('get_pelanggaran/', views.get_pelanggaran)
]