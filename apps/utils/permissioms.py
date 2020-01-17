# -*- coding: utf-8 -*-
from rest_framework import permissions


class OrderHasUserOrReadOnly(permissions.BasePermission):
    """
    订单相关人员权限判定 - 指定 乘客 / 司机
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.initiator == request.user


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
