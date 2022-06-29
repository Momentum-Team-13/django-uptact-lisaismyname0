from django.db import models
from django.core.validators import RegexValidator
from django.forms import BooleanField
from localflavor.us.models import USStateField, USZipCodeField
from django.utils import timezone
from users.models import User
# order is import python, import django, and then import from your own project


class Contact(models.Model):
    phone_regex = RegexValidator(
        regex=r'^\+?\d{10}$',
        message="Phone number must be entered in the format: '+9999999999'.")

    name = models.CharField(max_length=255)
    birthday = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=11,
                                    validators=[phone_regex],
                                    null=True,
                                    blank=True)
    address_1 = models.CharField(max_length=255, null=True, blank=True)
    address_2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = USStateField(null=True, blank=True)
    zip_code = USZipCodeField(null=True, blank=True)

    def __str__(self):
        return self.name


class Note(models.Model):
    text_field = models.CharField(max_length=255, null=True, blank=True)
    contact = models.ForeignKey(
        "Contact", on_delete=models.CASCADE, related_name="contact_notes", blank=True, null=True)
    delete_button = models.BooleanField(null=True)

    def __str__(self):
        return f"{self.text_field}"


class Favorite(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="favorites")
    contact = models.ForeignKey(
        Contact, on_delete=models.CASCADE, related_name="favorites")
