from django.urls import path
from .views import get_post_details

urlpatterns = [

    path('get-post-details/', get_post_details, name="get-post-details"),
]