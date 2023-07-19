# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.simulate_match, name='simulate_match'),
]
