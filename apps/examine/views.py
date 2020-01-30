from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from examine.models import ExamineLog, DriverProfile
from examine.serializer import DriverProfileSerializer, ExamineLogSerializer, UpdateExamineLogSerializer


class VerifyIdentyInfo(mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    '''
    create:
        上传车主审核信息

    retrieve:
        获取车主审核进度
    '''
    permission_classes = (IsAuthenticated,)
    serializer_class = ExamineLogSerializer

    # 车主审核的图片
    def create(self, request, *args, **kwargs):
        user = request.user
        f_id_card = request.FILES.get("f_id_card")
        b_id_card = request.FILES.get("b_id_card")
        driver_license = request.FILES.get("license")
        f_car = request.FILES.get("f_car")
        l_car = request.FILES.get("l_car")
        r_car = request.FILES.get("r_car")

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
            return Response({"error": "上传信息不足"})

    # 查看当前的审核进度
    def retrieve(self, request, *args, **kwargs):
        user = request.user

        user_info = DriverProfile.objects.filter(user_id=user).first()
        if user_info:
            ser = DriverProfileSerializer(instance=user_info)
            return Response(ser.data)
        else:
            return Response({"error": "司机信息不存在"})


class UpdateVerifyIdentyInfo(mixins.CreateModelMixin, viewsets.GenericViewSet):
    '''
    create:
        修改司机的审核信息
    '''
    permission_classes = (IsAuthenticated,)
    serializer_class = ExamineLogSerializer

    # 修改审核的图片
    def create(self, request, *args, **kwargs):
        user = request.user
        f_id_card = request.FILES.get("f_id_card")
        b_id_card = request.FILES.get("b_id_card")
        driver_license = request.FILES.get("license")
        f_car = request.FILES.get("f_car")
        l_car = request.FILES.get("l_car")
        r_car = request.FILES.get("r_car")
        driver_user = DriverProfile.objects.get(user_id=user)

        car_user = ExamineLog.objects.filter(applicant=driver_user).first()
        if car_user:
            car_user = car_user
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
            car_user.save()
            ser = DriverProfileSerializer(instance=driver_user)
            return Response(ser.data)
        else:
            return Response({"error": "未开通司机验证"})
