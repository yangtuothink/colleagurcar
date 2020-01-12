from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from rest_framework import permissions, viewsets, mixins
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ViewSet

from common.keys import AD_CAROUSEL_PAGES
from examine.models import ExamineLog
from users.models import UserProfile
from users.serializer import *
from utils.http import render_success, render_fail

User = get_user_model()


# Create your views here.
class CustomBackend(ModelBackend):
    """
    自定义用户验证
    """

    def authenticate(self, username=None, password=None, **kwargs):
        try:
            # 用户名和手机都能登录
            user = User.objects.get(
                Q(username=username) | Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class UserInfoOption(mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.ViewSet):
    '''
    create:
        创建用户 必要参数:

        字段中文    字段英文         是否必传
        昵称        nick_name       是
        用户名称    username        是
        密码        password       是


    retrieve:
        获取用户 必要参数

        字段中文    字段英文      是否必传
        用户id    id             是


    '''
    permission_classes = (IsAuthenticated,)

    # 创建用户
    def create(self, request, *args, **kwargs):
        user = UserProfile()
        user.nick_name = request.POST.get("nick_name")
        user.username = request.POST.get("username")
        user.password = make_password(request.POST.get("password"))
        user.save()
        ret = UserProfileSerializer(user)
        return Response(ret.data)

    # 获取用户id的资料
    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        user = UserProfile.objects.filter(id=pk)
        curr_user = request.user
        if user.exists():
            if curr_user != user.first():
                ser = UserOtherSerializer(instance=user.first())
            else:
                ser = UserProfileSerializer(instance=curr_user)
            return Response(ser.data)
        else:
            ret = render_fail("未找到用户")
            return Response(ret)


class ModifyUserInfo(mixins.CreateModelMixin, viewsets.ViewSet):
    '''
    create:
        创建用户 必要参数:

        字段中文    字段英文         是否必传
        用户图片     user_avatar      否
        昵称        nick_name        否

    '''

    permission_classes = (IsAuthenticated,)
    # 用户修改信息
    def create(self, request, *args, **kwargs):
        img_icon = request.FILES.get("user_avatar")
        nick_name = request.POST.get("nick_name")
        user = request.user
        if img_icon:
            user.image = img_icon
        if nick_name:
            user.nick_name = nick_name
        user.save()
        ret = UserProfileSerializer(user)
        return Response(ret.data)


class BannerViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    '''
        list:
            获取轮播图列表 必要参数:

            无
    '''
    queryset = Banner.objects.all().order_by("index")[:AD_CAROUSEL_PAGES]
    serializer_class = BannerSerializer
