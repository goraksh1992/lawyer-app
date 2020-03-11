from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from user.models import AppointmentsModel, UserModel
from .serializers import (
    SimpleAppointmentSerializer,
    SimpleLawyerSerializer
)
from .models import LawyerModel


@api_view(['GET'])
def get_lawyer_appointments(request, lawyer_id):
    fields = ('id', 'user_id', 'app_date', 'app_time', 'app_status')
    lawyer_app = AppointmentsModel.objects.filter(lawyer_id=lawyer_id)
    serializer = SimpleAppointmentSerializer(lawyer_app, many=True, fields=fields)
    return Response(
        data={"status": status.HTTP_200_OK, "message": "Appointments details", "appDetails": serializer.data},
        status=status.HTTP_200_OK)


@api_view(['GET'])
def get_lawyer_appointment_details(request, id):
    try:
        appointDetails = AppointmentsModel.objects.get(pk=id)
    except AppointmentsModel.DoesNotExist:
        Response(data={"status": status.HTTP_204_NO_CONTENT, "message": "Record not found"},
                 status=status.HTTP_204_NO_CONTENT)
    serialize = SimpleAppointmentSerializer(appointDetails)
    return Response(data={"status": status.HTTP_200_OK, "message": "Appointment detail", "appDetails": serialize.data})


@api_view(['PUT'])
def reschedule_appointment(request, id):
    try:
        appDetails = AppointmentsModel.objects.get(pk=id)
    except AppointmentsModel.DoesNotExist:
        return Response(data={"status": status.HTTP_204_NO_CONTENT, "message": "No record found"},
                        status=status.HTTP_204_NO_CONTENT)
    serializer = SimpleAppointmentSerializer(appDetails, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={"status": status.HTTP_200_OK, "message": "appointment rescheduled"},
                        status=status.HTTP_200_OK)
    return Response(data={"status": status.HTTP_400_BAD_REQUEST, "message": "fail to reschedule appointment"},
                    status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def accept_reject_appointment(request, id):
    fields = ('app_status')
    try:
        appDetails = AppointmentsModel.objects.get(pk=id)
    except:
        return Response(data={"status": status.HTTP_404_NOT_FOUND, "message": "Record not found"})

    serializer = SimpleAppointmentSerializer(appDetails, data=request.data, fields=fields)
    if serializer.is_valid():
        if serializer.save():
            return Response(data={"status": status.HTTP_200_OK, "message": "Appointment status updated"})
        else:
            return Response(data={"status": status.HTTP_400_BAD_REQUEST, "message": "Error"})

    return Response(data={"status": status.HTTP_400_BAD_REQUEST, "message": "Bad Request"})


@api_view(['POST'])
def lawyer_login(request):
    fields = ('id', 'full_name', 'email', 'contact', 'profile_image', 'state', 'city')
    try:
        lawyer_details = LawyerModel.objects.get(email=request.data['email'], password=request.data['password'])
    except LawyerModel.DoesNotExist:
        return Response(data={"status": status.HTTP_203_NON_AUTHORITATIVE_INFORMATION,
                              "message": "Invalid credentials"})
    serializer = SimpleLawyerSerializer(lawyer_details, fields=fields)
    return Response(
        data={"status": status.HTTP_200_OK, "message": "Valid credentials", "lawyerDetails": serializer.data})


@api_view(['GET'])
def get_lawyer_profile(request, id):
    fields = ('full_name', 'contact', 'email', 'address', 'gender', 'birth_date', 'city', 'state',
              'pincode', 'profile_image')
    try:
        lawyerDetails = LawyerModel.objects.get(pk=id)
    except LawyerModel.DoesNotExist:
        return Response(data={"status": status.HTTP_204_NO_CONTENT, "message": "Not found"},
                        status=status.HTTP_204_NO_CONTENT)
    serializer = SimpleLawyerSerializer(lawyerDetails, fields=fields)
    return Response(data={"status": status.HTTP_200_OK, "message": "lawyer detail", "lawyerDetails": serializer.data},
                    status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_lawyer_details(request, id):
    try:
        lawyerDetail = LawyerModel.objects.get(pk=id)
    except LawyerModel.DoesNotExist:
        return Response(data={"status": status.HTTP_204_NO_CONTENT, "message": "No record found"})

    serializer = SimpleLawyerSerializer(lawyerDetail, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={"status": status.HTTP_200_OK, "message": "Record updated successfully  "})

    return Response(data={"status": status.HTTP_400_BAD_REQUEST})


@api_view(['GET'])
def get_lawyer_details(request):
    fields = ('full_name', 'contact', 'email', 'address', 'gender', 'birth_date', 'city', 'state',
              'pincode', 'profile_image')
    lawyerDetails = LawyerModel.objects.all()
    serializer = SimpleLawyerSerializer(lawyerDetails, many=True, fields=fields)
    return Response(data={"status": status.HTTP_200_OK, "message": "Lawyer details", "lawyerDetails": serializer.data})
