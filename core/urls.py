from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('', views.handle_index),
    path('contacts/', views.handle_contacts),
    path('about/', views.handle_about),

    path('admin/', admin.site.urls)
]
