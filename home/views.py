from django.shortcuts import render, redirect
from .forms import PersonForm

def home(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = PersonForm()

    return render(request, 'home/home.html', {'form': form})

def success(request):
    return render(request, 'home/success.html')