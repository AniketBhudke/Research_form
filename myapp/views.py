from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm
import pandas as pd
from django.db import models
from .models import Contact

def Contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)   # form filled with POST data
        if form.is_valid():
            contact = form.save()
            purposes = request.POST.getlist('purposes')  # ✅ This is already a Python list
        
            contact.save()   
            return redirect('success')
            return HttpResponse("Form submitted successfully!")                # save to DB # go to success page
    else:
        form = ContactForm()              # empty form for GET request

    return render(request, 'myapp/contact.html', {'form': form})

def success_view(request):
        return render(request, 'myapp/success.html')

# def export_contacts_csv(request):
#     # Create the HttpResponse object with CSV headers
#     response = HttpResponse(
#         content_type='text/csv',
#         headers={'Content-Disposition': 'attachment; filename="contacts.csv"'},
#     )

#     writer = csv.writer(response)
    
#     # Write the header row
#     writer.writerow(['Name', 'Email', 'Year', 'Department', 'Tools', 'Purposes', 'Accuracy'])
    
#     # Fetch all contacts from DB
#     contacts = Contact.objects.all()
    
#     # Write data rows
#     for contact in contacts:
#         writer.writerow([
#             contact.name,
#             contact.email,
#             contact.year,
#             contact.department,
#             contact.tools,
#             ", ".join(contact.purposes),  # assuming purposes is a list
#             contact.accuracy
#         ])
    
#     return response
