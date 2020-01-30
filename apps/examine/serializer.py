from rest_framework import serializers

from examine.models import ExamineLog, DriverProfile
from users.serializer import UserProfileSerializer


class ExamineLogSerializer(serializers.ModelSerializer):
    applicant = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    license = serializers.ImageField(help_text="驾照", required=True)
    f_id_card = serializers.ImageField(help_text="身份证正面照", required=True)
    b_id_card = serializers.ImageField(help_text="身份证背面照", required=True)
    f_car = serializers.ImageField(help_text="车正面照", required=True)
    l_car = serializers.ImageField(help_text="车左侧照", required=True)
    r_car = serializers.ImageField(help_text="车后侧照", required=True)
    status = serializers.IntegerField(help_text="状态", label="当前状态", read_only=True)
    
    class Meta:
        model = ExamineLog
        # fields = "__all__"
        exclude = ("add_time",)


class UpdateExamineLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamineLog
        fields = "__all__"


class DriverProfileSerializer1(serializers.ModelSerializer):
    class Meta:
        model = DriverProfile
        fields = "__all__"


class DriverProfileSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    examine_log = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        user_info_ser = UserProfileSerializer(instance=obj.user_id)
        return user_info_ser.data
    
    def get_examine_log(self, obj):
        driver_examinelog = ExamineLog.objects.get(applicant=obj)
        ser = UpdateExamineLogSerializer(instance=driver_examinelog)
        return ser.data
    
    class Meta:
        model = DriverProfile
        exclude = ["add_time"]
