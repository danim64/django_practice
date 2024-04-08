from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('<month>', views.monthly_challenge),

]