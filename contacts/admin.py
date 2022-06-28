from django.contrib import admin
from .models import Contact
from .models import Favorite
from .models import Note

admin.site.register(Contact)
# MODEL NAMES ARE ALWAYS SINGULAR
admin.site.register(Favorite)
admin.site.register(Note)
