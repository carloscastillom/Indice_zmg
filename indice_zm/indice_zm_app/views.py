from django.shortcuts import render
from .models import indiceDB 

def home(request):
    all_letters = indiceDB.objects.all()
    return render(request, 'index.html', {'all_letters': all_letters})

