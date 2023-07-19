from django.urls import path
from . import views

app_name = 'quadratic_equation_solver'

urlpatterns = [
    path('', views.quadratic_equation_solver, name='quadratic_equation_solver'),
]
