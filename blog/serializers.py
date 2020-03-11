from rest_framework import serializers
from .models import BlogModel, BlogCommentModel, BlogLikeModel


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = '__all__'


class BlogCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCommentModel
        fields = '__all__'


class BlogLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogLikeModel
        fields = '__all__'



