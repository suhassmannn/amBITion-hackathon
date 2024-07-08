from django.contrib import admin
from NGO.models import ngos
from Users.models import Volunteer

# admin.site.register(categories)
admin.site.register(ngos)
admin.site.register(Volunteer)