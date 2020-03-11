from rest_framework import serializers
from .models import LawyerModel
from user.models import AppointmentsModel, LawyerFeedback


class LawyerSerializer(serializers.ModelSerializer):
    # class Meta:
    #     model = LawyerModel
    #     fields = '__all__'
    # Below code for only access specific database fields, which you want to access
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)

        super(LawyerSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class SimpleLawyerSerializer(LawyerSerializer):
    class Meta:
        model = LawyerModel
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)

        super(AppointmentSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class SimpleAppointmentSerializer(AppointmentSerializer):
    class Meta:
        model = AppointmentsModel
        fields = '__all__'

