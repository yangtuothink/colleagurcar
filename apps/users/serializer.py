# -*- coding: utf-8 -*-
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

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
    image = serializers.ImageField(help_text="用户图像")
    nick_name = serializers.CharField(help_text="昵称")
    username = serializers.CharField(required=False, help_text="用户名")

    class Meta:
        model = UserProfile
        exclude = ["password", "date_joined", "is_superuser"]


class UserRegSerializer(serializers.ModelSerializer):
    nick_name = serializers.CharField(default="",
                                      help_text="昵称")

    username = serializers.CharField(help_text="用户名",
                                     required=True,
                                     validators=[
                                         UniqueValidator(queryset=UserProfile.objects.all(), message="用户已经存在")],
                                     error_messages={
                                         "required": "请输入用户名",
                                     })
    password = serializers.CharField(required=True,
                                     error_messages={
                                         "required": "请输入用户名",
                                     }, help_text="密码", write_only=True)

    def validate(self, attrs):
        attrs["password"] = make_password(attrs["password"])
        return attrs

    class Meta:
        model = UserProfile
        fields = ("nick_name", "username", "password", "image")


class UserUpdateSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(label="用户图像", required=False, help_text="用户图像")
    class Meta:
        model = UserProfile
        fields = ["image", "nick_name", "mobile"]


class CustomerMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerMessage
        fields = "__all__"


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"
