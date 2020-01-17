# _*_ coding:utf-8 _*_
__author__ = "yangtuo"
__date__ = "2019/4/12 15:07"

import django_filters
from .models import DriverOrder, CustomerOrder


class DriverOrderFilter(django_filters.rest_framework.FilterSet):
    p_sum = django_filters.NumberFilter(field_name="p_sum", lookup_expr='gte')
    label_type = django_filters.ChoiceFilter(choices=(("m", "上班"), ("n", "下班")))
    origin = django_filters.CharFilter(field_name="origin", lookup_expr='icontains')
    finish = django_filters.CharFilter(field_name="finish", lookup_expr='icontains')

    class Meta:
        model = DriverOrder
        fields = ["p_sum", "label_type", "origin", "finish"]


class CustomerOrderFilter(django_filters.rest_framework.FilterSet):
    label_type = django_filters.ChoiceFilter(choices=(("m", "上班"), ("n", "下班")))
    origin = django_filters.CharFilter(field_name="origin", lookup_expr='icontains')
    finish = django_filters.CharFilter(field_name="finish", lookup_expr='icontains')
    
    class Meta:
        model = CustomerOrder
        fields = ["label_type", "origin", "finish"]
