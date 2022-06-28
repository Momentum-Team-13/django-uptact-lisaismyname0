from django.contrib import admin
from .models import Contact
from .models import Favorite

admin.site.register(Contact)
# MODEL NAMES ARE ALWAYS SINGULAR
admin.site.register(Favorite)
