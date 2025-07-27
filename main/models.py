from django.db import models

class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)  # Store phone numbers in E.164 format
    tour_type = models.CharField(max_length=100)
    tour_location = models.CharField(max_length=100)
    number_of_persons = models.IntegerField()
    travel_date = models.DateField()
    email = models.EmailField()

    def __str__(self):
        return self.name
