from django.shortcuts import render

# Create your views here.
def randommathgenerator(request):
    
    return render(request, 'mathgen.html')