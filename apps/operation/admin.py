from django.contrib import admin
from operation.models import CustomerMessage, DriverMessage, ChatMessage, CourseComments, FoulLog, CancelLog

# Register your models here.

admin.site.register(CustomerMessage)
admin.site.register(DriverMessage)
admin.site.register(ChatMessage)
admin.site.register(CourseComments)
admin.site.register(FoulLog)
admin.site.register(CancelLog)
