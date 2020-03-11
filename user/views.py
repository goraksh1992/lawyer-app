from django.shortcuts import render
from .serializers import UserSerializer, LawyerFeedbackSerializer
from lawyer_panel.serializers import AppointmentSerializer
from .models import UserModel, AppointmentsModel
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['POST'])
def userRegistration(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={"status": status.HTTP_200_OK, "message": "Welcome to Lawyer App, you have registered "
                                                                       "successfully."}, status=status.HTTP_200_OK)
    return Response(data={"status": status.HTTP_400_BAD_REQUEST, "message": serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def updateUserDetails(request, user_id):
    try:
        userDetails = UserModel.objects.get(pk=user_id)
    except UserModel.DoesNotExist:
        return Response(data={"status": status.HTTP_404_NOT_FOUND, "message": "Not user found"})

    serializer = UserSerializer(userDetails, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={"status": status.HTTP_200_OK, "message": "User details updated!"}, status=status.HTTP_200_OK)
    return Response(data={"status": status.HTTP_400_BAD_REQUEST, "message": "Error..Please try again"})


@api_view(['POST'])
def add_lawyer_feedback(request):
    serializer = LawyerFeedbackSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={"status": status.HTTP_200_OK, "message": "Feedback added"}, status=status.HTTP_200_OK)
    return Response(data={"status": status.HTTP_400_BAD_REQUEST, "message": "Failed to add feeback"},
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_lawyer_appointment(request):
    serializer = AppointmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={"status": status.HTTP_200_OK, "message": "Rescheduled appointments"}, status=status.HTTP_200_OK)
    return Response(data={"status": status.HTTP_400_BAD_REQUEST, "message": "Appointment error"})


