# -*- coding: utf-8 -*-
from rest_framework import permissions
from order.models import DriverOrder, CustomerOrder, CancelLog, ChatMessage, CourseComments


class CommentsReadOnly(permissions.BasePermission):
    """
    评论权限
    """
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif CourseComments.objects.filter(order__initiator=request.user):
            return True
        return False


class IsOrderCustomer(permissions.BasePermission):
    """
    订单相关乘客 权限判定
    """
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.initiator == request.user and request.user.is_driver == "n"


class IsOrderDriver(permissions.BasePermission):
    """
    订单相关司机 权限判定
    """
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.initiator == request.user and request.user.is_driver == "y"
