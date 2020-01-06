from rest_framework.authentication import BaseAuthentication
from rest_framework_jwt.authentication import jwt_decode_handler

from users.models import UserProfile


class Authentication(BaseAuthentication):
    '''用于用户登录验证'''
    def authenticate(self, request):
        token = request._request.GET.get('token')
        toke_user = jwt_decode_handler(token)
        # 获得user_id
        user_id = toke_user["user_id"]
        # 通过user_id查询用户信息
        user = UserProfile.objects.get(pk=user_id)

        return user, token

    def authenticate_header(self, request):
        pass
