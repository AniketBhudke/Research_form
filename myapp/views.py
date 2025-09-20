from django.shortcuts import render, redirect
from .forms import ContactForm
import pandas as pd

def Contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)   # form filled with POST data
        if form.is_valid():
            form.save()                   # save to DB
            return redirect('success') # go to success page
    else:
        form = ContactForm()              # empty form for GET request

    return render(request, 'myapp/contact.html', {'form': form})

def success_view(request):
        return render(request, 'myapp/success.html')

