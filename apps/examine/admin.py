from django.contrib import admin

# Register your models here.
from examine.models import DriverProfile, ExamineLog, FoulRule, FoulLog, DriverMessage

admin.site.register(DriverProfile)
admin.site.register(DriverMessage)
admin.site.register(ExamineLog)
admin.site.register(FoulRule)
admin.site.register(FoulLog)
