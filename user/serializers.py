from rest_framework import serializers
from .models import UserModel, LawyerFeedback


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'


class LawyerFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = LawyerFeedback
        fields = '__all__'
