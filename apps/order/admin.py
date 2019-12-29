from django.contrib import admin

# Register your models here.
from order.models import Order, DriverSquare, CustomerSquare, CancelLog, ChatMessage, CourseComments

admin.site.register(Order)
admin.site.register(DriverSquare)
admin.site.register(CustomerSquare)
admin.site.register(CancelLog)
admin.site.register(ChatMessage)
admin.site.register(CourseComments)
