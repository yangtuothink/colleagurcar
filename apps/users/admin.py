from django.contrib import admin

# Register your models here.
from users.models import UserProfile, Banner

admin.site.register(UserProfile)
admin.site.register(Banner)
