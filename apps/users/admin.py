from django.contrib import admin

# Register your models here.
from users.models import UserProfile, Banner, BankCard, CustomerMessage

admin.site.register(UserProfile)
admin.site.register(Banner)
admin.site.register(BankCard)
admin.site.register(CustomerMessage)
