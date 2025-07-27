# main/forms.py
from django import forms
from .models import Enquiry  # Import the Enquiry model

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ['name', 'contact', 'tour_type', 'tour_location', 'number_of_persons', 'travel_date', 'email']
    
    # Custom widget for the name field
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ''}))
    
    # Custom widget for the contact field
    contact = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ''}))
    
    # Custom dropdown (choice field) for tour type
    tour_type = forms.ChoiceField(
        choices=[('Hill Stations', 'Hill Stations'), 
                 ('Ecotourism', 'Ecotourism'), 
                 ('Beaches', 'Beaches'), 
                 ('Religious', 'Religious')],
        widget=forms.Select(attrs={'placeholder': 'Select tour type'})
    )
    
    # Custom widget for the tour location field
    tour_location = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ''}))
    
    # Custom widget for the number of persons field
    number_of_persons = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': ''}))
    
    # Custom widget for the travel date field
    travel_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'placeholder': ''}))
    
    # Custom widget for the email field
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': ''}))
