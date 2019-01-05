from django.contrib import admin
from .models import Profile

# This statement registers the Profile model to admin panel

admin.site.register(Profile)