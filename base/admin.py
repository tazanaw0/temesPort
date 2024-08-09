from django.contrib import admin
from .models import Photo

#Making our Photo Model available in our admin portal 
admin.site.register(Photo)
