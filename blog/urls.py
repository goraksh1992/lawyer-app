from django.urls import path
from .views import get_blog_details_view, add_blog_comment, like_blog

urlpatterns = [

    path("get-blog-details/", get_blog_details_view, name="get-blog-details"),
    path('add-blog-comment', add_blog_comment, name="add-blog-comment"),
    path('like-blog', like_blog, name="like-blog"),
]
