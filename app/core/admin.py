from django.contrib import admin

from .models.user import User
from .models.organization import Organization

# Register your models here.
admin.site.register(User)
admin.site.register(Organization)