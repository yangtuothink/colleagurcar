from django.contrib import admin

# Register your models here.
from order.models import DriverOrder, CustomerOrder, CancelLog, ChatMessage, CourseComments

admin.site.register(DriverOrder)
admin.site.register(CustomerOrder)
admin.site.register(CancelLog)
admin.site.register(ChatMessage)
admin.site.register(CourseComments)
