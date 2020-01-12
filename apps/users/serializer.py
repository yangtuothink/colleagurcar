# -*- coding: utf-8 -*-

from rest_framework import serializers
from .models import UserProfile, BankCard, CustomerMessage, Banner


class BankCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankCard
        fields = "__all__"


class UserProfileSerializer(serializers.ModelSerializer):
    banks = serializers.SerializerMethodField()

    def get_banks(self, obj):
        user_banks = BankCard.objects.filter(user=obj.id).all()
        ret = []
        for item in user_banks:
            ret.append({"bankId": item.card_num, "bankName": item.bank})
        return ret

    class Meta:
        model = UserProfile
        exclude = ["password", "date_joined", "is_superuser"]


# 获取其他用户的信息
class UserOtherSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = UserProfile
        exclude = ["password", "date_joined", "is_superuser"]


class CustomerMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerMessage
        fields = "__all__"


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"
