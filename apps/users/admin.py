# django
from django.contrib import admin

# project
from apps.users.models import User

admin.site.register(User)

