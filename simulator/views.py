
# views.py
from django.shortcuts import render
from django.http import JsonResponse
import random

def simulate_match(request):

    return render(request, 'football_simulator.html')
