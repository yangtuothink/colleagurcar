from rest_framework import serializers

from examine.models import ExamineLog, DriverProfile
from users.models import UserProfile
from users.serializer import UserProfileSerializer


class ExamineLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamineLog
        fields = "__all__"


class DriverProfileSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    examine_log = serializers.SerializerMethodField()

    def get_user(self, obj):
        user_info_ser = UserProfileSerializer(instance=obj.user_id)
        return user_info_ser.data

    def get_examine_log(self, obj):
        driver_examinelog = ExamineLog.objects.get(applicant=obj)
        ser = ExamineLogSerializer(instance=driver_examinelog)
        return ser.data

    class Meta:
        model = DriverProfile
        exclude = ["add_time"]
