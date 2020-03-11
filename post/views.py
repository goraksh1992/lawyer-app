from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import PostModel
from .serializers import PostSerializer
from rest_framework import status


@api_view(['GET'])
def get_post_details(request):
    postDetails = PostModel.objects.all()
    serializer = PostSerializer(postDetails, many=True)
    return Response(data={"status": status.HTTP_200_OK, "message": "Post details", "postDetails": serializer.data})