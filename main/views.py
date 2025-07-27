from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import EnquiryForm
from .models import Enquiry
from twilio.rest import Client
from django.conf import settings

# Home page with enquiry form handling
def home(request):
    success = False
    if request.method == "POST":
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()  # Save the enquiry form data to the database
            success = True
    else:
        form = EnquiryForm()
    return render(request, 'home.html', {'form': form, 'success': success})

# View to list all enquiries
def enquiry_list(request):
    enquiries = Enquiry.objects.all().order_by('-created_at')  # Order by most recent
    return render(request, 'enquiry_list.html', {'enquiries': enquiries})

# Search functionality
def search(request):
    query = request.GET.get('query', '')  # Get the search term from the request
    # Replace with your search logic; currently, it just returns the query
    return render(request, 'search_results.html', {'query': query})

# User registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}!")
            return redirect('login')  # Redirect to login page after registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
