from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from examine.models import ExamineLog
from examine.serializer import ExamineLogSerializer
from utils.http import render_fail, render_success


class VerifyIdentyInfo(GenericViewSet):

    # 车主审核的图片
    def post_owner_information(self, request):
        user = request.user
        f_id_card = request.FILES.get("IdCardFront")
        b_id_card = request.FILES.get("IdCardBehind")
        driver_license = request.FILES.get("Driver")
        f_car = request.FILES.get("CardFront")
        l_car = request.FILES.get("CardSide")
        r_car = request.FILES.get("CardBehind")

        if f_id_card and b_id_card and driver_license and f_car and l_car and r_car:
            car_user = ExamineLog()
            car_user.applicant = user
            car_user.license = driver_license
            car_user.f_id_card = f_id_card
            car_user.b_id_card = b_id_card
            car_user.f_car = f_car
            car_user.l_car = l_car
            car_user.r_car = r_car
            car_user.save()

            res = {
                "user": user,
                "status": car_user.status
            }
            ret = render_success(data=res)
            return Response(ret)

        else:
            code = "上传信息不足"
            ret = render_fail(code)
            return Response(ret)

    # 查看当前的审核进度
    def get_current_progress(self, request):
        user = request.user
        car_user = ExamineLog(applicant=user)
        res = ExamineLogSerializer(instance=car_user)
        ret = render_success(data=res)
        return Response(ret)

    # 修改审核的图片
    def modify_examine_photo(self, request):
        user = request.user
        f_id_card = request.FILES.get("IdCardFront")
        b_id_card = request.FILES.get("IdCardBehind")
        driver_license = request.FILES.get("Driver")
        f_car = request.FILES.get("CardFront")
        l_car = request.FILES.get("CardSide")
        r_car = request.FILES.get("CardBehind")

        car_user = ExamineLog(applicant=user)
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

        res = {
            "user": user,
            "status": car_user.status
        }
        ret = render_success(data=res)
        return Response(ret)
