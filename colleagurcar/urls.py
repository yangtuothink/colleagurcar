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
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

# 使用 routers 的方式
from order.views import OrderView

router = DefaultRouter()

# 商品的 url
# 注册后就不需要每个都写一个 url 了.这样集合一个就可以了
router.register(r'orders', OrderView, basename='orders')

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'docs/', include_docs_urls(title="同事用车")),
    url(r'^', include(router.urls))
]



