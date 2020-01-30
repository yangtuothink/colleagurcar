from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from rest_framework import viewsets, mixins, permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler

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
    serializer_class = UserRegSerializer
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return UserProfileSerializer
        elif self.action == "create":
            return UserRegSerializer

        return UserProfileSerializer

    def get_permissions(self):
        if self.action == "retrieve":
            return [permissions.IsAuthenticated()]
        elif self.action == "create":
            return []

        return []

    # 创建用户
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict["token"] = jwt_encode_handler(payload)
        re_dict["id"] = user.id

        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

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

    def perform_create(self, serializer):
        return serializer.save()


class ModifyUserInfo(mixins.CreateModelMixin, viewsets.GenericViewSet):
    '''
    create:
        修改用户信息
    '''

    permission_classes = (IsAuthenticated,)
    serializer_class = UserUpdateSerializer

    # 用户修改信息
    def create(self, request, *args, **kwargs):
        image = request.data.get("image")
        nick_name = request.data.get("nick_name")
        mobile = request.data.get("mobile")
        user = request.user
        if image:
            user.image = image
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
