from django.shortcuts import render
from .serializers import BlogSerializer, BlogCommentSerializer, BlogLikeSerializer
from rest_framework.decorators import api_view
from .models import BlogModel, BlogLikeModel
from rest_framework.response import Response
from rest_framework import status
from lawyer_panel.models import LawyerModel


@api_view(['GET'])
def get_blog_details_view(request):
    blog = BlogModel.objects.all()
    serializer = BlogSerializer(blog, many=True)
    return Response(data=serializer.data)


@api_view(['POST'])
def add_blog_comment(request):
    serializer = BlogCommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        blog = BlogModel.objects.get(pk=request.data['blog_id'])
        data = {"comment_count": blog.comment_count + 1}
        serializer1 = BlogSerializer(blog, data=data, partial=True)
        if serializer1.is_valid():
            serializer1.save()
        return Response(data={"status": status.HTTP_200_OK, "message": "Comment added", "data": serializer.data})

    return Response(data={"status": status.HTTP_400_BAD_REQUEST, "message": "Bad request"})


@api_view(['POST'])
def like_blog(request):
    checkLike = BlogLikeModel.objects.filter(blog_id = request.data['blog_id'], user_id = request.data['user_id'])
    if checkLike:
        getBlog = BlogModel.objects.get(pk=request.data['blog_id'])
        data = {"like_count": getBlog.like_count - 1}
        serializer2 = BlogSerializer(getBlog, data=data, partial=True)
        if serializer2.is_valid():
            serializer2.save()
            checkLike.delete()
        return Response(data={"status": status.HTTP_200_OK, "message": "Blog disliked"})
    else:
        serializer = BlogLikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            getBlog = BlogModel.objects.get(pk=request.data['blog_id'])
            data = {"like_count": getBlog.like_count + 1}
            serializer2 = BlogSerializer(getBlog, data=data, partial=True)
            if serializer2.is_valid():
                serializer2.save()
            return Response(data={"status": status.HTTP_200_OK, "message": "Blog liked"})

    return Response(data={"status": status.HTTP_400_BAD_REQUEST, "message": "Bad request"})

