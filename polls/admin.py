from django.contrib import admin

from .models import Address
from .models import Permission

# Register your models here.

admin.site.register(Address)
admin.site.register(Permission)