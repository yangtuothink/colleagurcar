from rest_framework import serializers

from examine.models import ExamineLog


class ExamineLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamineLog
        fields = "__all__"
