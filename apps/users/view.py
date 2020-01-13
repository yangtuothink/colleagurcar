from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError
from django.db.models import Q
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from common.keys import AD_CAROUSEL_PAGES
from users.serializer import *

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


class UserInfoOption(mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    '''
    create:
        创建用户

    retrieve:
        获取用户
    '''
    serializer_class = CreateUserProfile

    def get_permissions(self):
        if self.action != "create":
            return [IsAuthenticated(), ]
        return []

    # 创建用户
    def create(self, request, *args, **kwargs):
        user = UserProfile()
        nick_name = request.POST.get("nick_name")
        username = request.POST.get("username")
        password = make_password(request.POST.get("password"))

        if nick_name and username and password:
            user.nick_name = nick_name
            user.username = username
            user.password = password
            try:
                user.save()
                ret = UserProfileSerializer(user)
                return Response(ret.data)
            except IntegrityError as e:
                return Response({"error": "用户已存在"})
        else:
            return Response({"error": "传入参数错误"})

    # 获取用户id的资料
    def retrieve(self, request, *args, **kwargs):
        print(request.user)
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
            return Response({"error": "未找到用户"})


class ModifyUserInfo(mixins.CreateModelMixin, viewsets.GenericViewSet):
    '''
    create:
        修改用户信息
    '''

    permission_classes = (IsAuthenticated,)
    serializer_class = UserOtherSerializer

    # 用户修改信息
    def create(self, request, *args, **kwargs):
        img_icon = request.FILES.get("user_avatar")
        nick_name = request.POST.get("nick_name")
        mobile = request.POST.get("mobile")
        user = request.user
        if img_icon:
            user.image = img_icon
        if nick_name:
            user.nick_name = nick_name
        if mobile:
            user.mobile = mobile
        user.save()
        ret = UserProfileSerializer(user)
        return Response(ret.data)


class BannerViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    '''
        list:
            获取轮播图列表
    '''
    queryset = Banner.objects.all().order_by("index")[:AD_CAROUSEL_PAGES]
    serializer_class = BannerSerializer
