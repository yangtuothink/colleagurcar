from django.conf.urls import url

from users.view import *

urlpatterns = [
    url(r"modify/", UserOption.as_view({"post": "modify_user_info", "get": "get_user_profile"})),
    url(r'create/', UserRegister.as_view()),
    url(r'describeOtherInfo/', OtherUser.as_view({"get": "get_other_info"})),

]
