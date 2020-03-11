from django.urls import path
from .views import FileUploadView, GetGalleryImages

urlpatterns = [

    path('upload-gallary-images', FileUploadView.as_view(), name="upload-gallary-images"),
    path('get-gallery-images', GetGalleryImages.as_view(), name="get-gallery-images"),
]