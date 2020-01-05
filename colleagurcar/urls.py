"""colleagurcar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

# 使用 routers 的方式
from rest_framework_jwt.views import obtain_jwt_token

from order.views import OrderView, CourseCommentsView, DriverSquareView, CustomerSquareView
from order.views import CancelLogView, ChatMessageView

router = DefaultRouter()

router.register(r'orders', OrderView, basename='orders')
router.register(r'comments', CourseCommentsView, basename='comments')
router.register(r'driver_square', DriverSquareView, basename='driver_square')
router.register(r'customer_square', CustomerSquareView, basename='customer_square')
router.register(r'cancel_log', CancelLogView, basename='cancel_log')
router.register(r'chat_message', ChatMessageView, basename='chat_message')

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'docs/', include_docs_urls(title="同事用车")),
    url(r'^', include(router.urls)),
    
    # 弃用 token 方式
    # url(r'^api-token-auth/', obtain_auth_token)
    
    # DRF JWT 认证
    url(r'^login/', obtain_jwt_token),
]
