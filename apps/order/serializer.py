# -*- coding: utf-8 -*-

from rest_framework import serializers
from .models import Order, DriverSquare, CustomerSquare


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class DriverSquareSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverSquare
        fields = "__all__"


class CustomerSquareSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerSquare
        fields = "__all__"
