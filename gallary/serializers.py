from rest_framework import serializers
from .models import GalleryModel


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryModel
        fields = "__all__"
