from django.contrib import admin
from .models import resourcegroup, resource, Hero
# Register your models here.

admin.site.register(resourcegroup)
admin.site.register(resource)
admin.site.register(Hero)