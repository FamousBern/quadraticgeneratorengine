from django.contrib import admin
from django.urls import path
from equations.views import generate_quadratic_equations

urlpatterns = [
    path('', generate_quadratic_equations, name='generate_quadratic_equations'),
]
