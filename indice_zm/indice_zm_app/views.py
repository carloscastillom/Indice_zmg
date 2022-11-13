from django.shortcuts import render
from .models import indiceDB 
from .forms import indiceform

def home(request):

    if request.method == "POST":
        form = indiceform(request.POST or None)
        if form.is_valid():
            form.save()
            all_letters = indiceDB.objects.all()
            return render(request, 'index.html', {'all_letters': all_letters})
    else:
        all_letters = indiceDB.objects.all()
        return render(request, 'index.html', {'all_letters': all_letters})

