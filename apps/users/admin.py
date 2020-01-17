from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _

from users.models import UserProfile, Banner, BankCard, CustomerMessage


class MyAdmin(UserAdmin):
    # 重写fieldsets在admin后台加入自己新增的字段
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('nick_name'), {'fields': ('nick_name',)}),
        (_('birday'), {'fields': ('birday',)}),
        (_('gender'), {'fields': ('gender',)}),
        (_('address'), {'fields': ('address',)}),
        (_('mobile'), {'fields': ('mobile',)}),
        (_('image'), {'fields': ('image',)}),
        (_('home'), {'fields': ('home',)}),
        (_('company_address'), {'fields': ('company_address',)}),
        (_('company'), {'fields': ('company',)}),
        (_('department'), {'fields': ('department',)}),
        (_('credit_score'), {'fields': ('credit_score',)}),
        (_('money'), {'fields': ('money',)}),
        (_('is_driver'), {'fields': ('is_driver',)}),
    )


admin.site.register(Banner)
admin.site.register(BankCard)
admin.site.register(CustomerMessage)
admin.site.register(UserProfile, MyAdmin)
