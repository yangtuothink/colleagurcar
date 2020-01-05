# -*- coding: utf-8 -*-
from rest_framework import permissions


class OrderHasUserOrReadOnly(permissions.BasePermission):
    """
    订单相关人员权限判定 - 指定 乘客 / 司机
    """
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.order__customer == request.user or obj.order__driver__user_id == request.user


class IsOrderCustomer(permissions.BasePermission):
    """
    订单相关乘客 权限判定
    """
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.order__customer == request.user


class IsOrderDriver(permissions.BasePermission):
    """
    订单相关司机 权限判定
    """
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.order__driver__user_id == request.user


class UserIsDriver(permissions.BasePermission):
    """
    司机行程广场 司机身份 权限判定
    """
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.initiator__user_id == request.user


class UserIsCustomer(permissions.BasePermission):
    """
    乘客行程广场 乘客身份 权限判定
    """
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.initiator == request.user
