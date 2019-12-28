from django.contrib import admin

# Register your models here.
from examine.models import DriverProfile, ExamineLog, FoulRule

admin.site.register(DriverProfile)
admin.site.register(ExamineLog)
admin.site.register(FoulRule)
