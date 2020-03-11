from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import GalleryModel

from .serializers import GallerySerializer


class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        gallary_serializer = GallerySerializer(data=request.data)

        if gallary_serializer.is_valid():
            gallary_serializer.save()
            return Response(gallary_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(gallary_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetGalleryImages(APIView):

    def get(self, request, *args, **kwargs):
        try:
            gallery = GalleryModel.objects.all()
        except GalleryModel.DoesNotExist:
            return Response(data={"status": status.HTTP_204_NO_CONTENT, "message": "Not found"})
        serializer = GallerySerializer(gallery, many=True)
        return Response(data={"status": status.HTTP_200_OK, "message": "Record found", "galleryDetails": serializer.data})


