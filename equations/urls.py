from django.contrib import admin
from django.urls import path
from equations.views import generate_quadratic_equations
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', generate_quadratic_equations, name='generate_quadratic_equations'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
