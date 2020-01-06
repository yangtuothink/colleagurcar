from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from common.keys import AD_CAROUSEL_PAGES
from common.user_auth import Authentication
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


class UserRegister(APIView):

    def post(self, request):
        user = UserProfile()
        user.nick_name = "qwp12"
        user.username = "122232"
        user.password = make_password("123456")
        user.save()
        ret = render_success()
        return Response(ret)


class UserOption(GenericViewSet):
    authentication_classes = [Authentication, ]

    # 用户修改信息
    def modify_user_info(self, request):
        img_icon = request.FILES.get("UserAvatar")
        nick_name = request.POST.get("NickName")
        user = request.user
        user.nick_name = nick_name
        user.image = img_icon
        user.save()
        ret = render_success()
        return Response(ret)

    # 获取用户的资料
    def get_user_profile(self, request):
        user = request.user
        ser = UserProfileSerializer(instance=user)
        ret = render_success(data=ser.data)
        return Response(ret)


class OtherUser(GenericViewSet):
    # 获取其他用户信息
    def get_other_info(self, request):
        uid = request.query_params.get("uid")
        user = UserProfile.objects.filter(pk=uid)
        if user.exists():
            ser = describeOtherInfo(instance=user.first())
            ret = render_success(data=ser.data)
            return Response(ret)
        else:
            code = "用户Id信息错误"
            ret = render_fail(code)
            return Response(ret)


class AdRecommendation(GenericViewSet):
    '''广告推荐接口'''

    def recommend_list(self, request):
        ad = Banner.objects.order_by("-index").all()[:AD_CAROUSEL_PAGES]
        data = BannerSerializer(instance=ad, many=True)
        ret = render_success(data=data)
        return Response(ret)