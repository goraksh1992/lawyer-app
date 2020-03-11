from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import SubscriptionModel
from rest_framework.views import APIView
from .serializers import SubscriptionSerializer


class GetSubscriptionDetails(APIView):

    def get(self, request, *args, **kwargs):
        try:
            subPlan = SubscriptionModel.objects.all()
        except SubscriptionModel.DoesNotExist:
            return Response(data={"status": status.HTTP_204_NO_CONTENT, "message": "Record not found"})

        serializer = SubscriptionSerializer(subPlan, many=True)
        return Response(data={"status": status.HTTP_200_OK, "message": "Record found", "subDetails": serializer.data})
