from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from examine.models import ExamineLog, DriverProfile
from examine.serializer import DriverProfileSerializer
from utils.http import render_fail


class VerifyIdentyInfo(mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.ViewSet):
    '''
    create:
        上传车主审核信息 必要参数:

            字段中文    字段英文         是否必传
            身份证前照   IdCardFront     是
            身份证后照   IdCardBehind    是
            驾驶证照     Driver          是
            汽车前照     CardFront       是
            汽车后照     CardBehind      是
            汽车侧照     CardSide        是

    retrieve:
        获取车主审核进度 必要参数:

            无
    '''
    permission_classes = (IsAuthenticated,)

    # 车主审核的图片
    def create(self, request, *args, **kwargs):
        user = request.user
        f_id_card = request.FILES.get("IdCardFront")
        b_id_card = request.FILES.get("IdCardBehind")
        driver_license = request.FILES.get("Driver")
        f_car = request.FILES.get("CardFront")
        l_car = request.FILES.get("CardSide")
        r_car = request.FILES.get("CardBehind")

        if f_id_card and b_id_card and driver_license and f_car and l_car and r_car:
            # 先创建一个司机信息
            driver_profile, _ = DriverProfile.objects.get_or_create(user_id=user)

            car_user, created = ExamineLog.objects.get_or_create(applicant=driver_profile)
            if created:
                car_user.license = driver_license
                car_user.f_id_card = f_id_card
                car_user.b_id_card = b_id_card
                car_user.f_car = f_car
                car_user.l_car = l_car
                car_user.r_car = r_car
                car_user.save()

            ser = DriverProfileSerializer(instance=driver_profile)
            return Response(ser.data)

        else:
            code = "上传信息不足"
            ret = render_fail(code)
            return Response(ret)

    # 查看当前的审核进度
    def retrieve(self, request, *args, **kwargs):
        user = request.user
        user_info = DriverProfile.objects.get(user_id=user)
        ser = DriverProfileSerializer(instance=user_info)
        return Response(ser.data)



class UpdateVerifyIdentyInfo(mixins.CreateModelMixin, viewsets.ViewSet):
    '''
    create:
        修改司机的审核信息

        字段中文    字段英文         是否必传
        身份证前照   IdCardFront     否
        身份证后照   IdCardBehind    否
        驾驶证照     Driver          否
        汽车前照     CardFront       否
        汽车后照     CardBehind      否
        汽车侧照     CardSide        否
    '''
    # 修改审核的图片
    def create(self, request, *args, **kwargs):
        user = request.user
        print(request.FILES)
        f_id_card = request.FILES.get("IdCardFront")
        b_id_card = request.FILES.get("IdCardBehind")
        driver_license = request.FILES.get("Driver")
        f_car = request.FILES.get("CardFront")
        l_car = request.FILES.get("CardSide")
        r_car = request.FILES.get("CardBehind")
        driver_user = DriverProfile.objects.get(user_id=user)

        car_user = ExamineLog.objects.filter(applicant=driver_user)
        if car_user.exists():
            if f_id_card:
                car_user.f_id_card = f_id_card
            if b_id_card:
                car_user.b_id_card = b_id_card
            if driver_license:
                car_user.license = driver_license
            if f_car:
                car_user.f_car = f_car
            if l_car:
                car_user.l_car = l_car
            if r_car:
                car_user.r_car = r_car
            car_user.first().save()
            ser = DriverProfileSerializer(instance=driver_user)
            return Response(ser.data)
        else:
            code = "未开通司机验证"
            ret = render_fail(code)
            return Response(ret)