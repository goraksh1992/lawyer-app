from django.db import models
from user.models import UserModel


class BlogModel(models.Model):

    status = (
        ("0", "Hold"),
        ("1", "Publish"),
    )

    def upload_image(self, filename):
        path = f"blog/blog_image/{filename}"
        return path

    blog_title = models.CharField(max_length=500, blank=False, null=False)
    blog_description = models.TextField(blank=False, null=False)
    blog_image = models.ImageField(upload_to=upload_image, blank=False, null=False)
    writer_name = models.CharField(max_length=200, blank=False, null=False)
    blog_status = models.CharField(max_length=50, choices=status)
    blog_date = models.DateTimeField(auto_now_add=True)
    like_count = models.IntegerField()
    comment_count = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.blog_title


class BlogCommentModel(models.Model):

    blog_id = models.ForeignKey(BlogModel, on_delete=models.CASCADE)
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    comment = models.TextField()
    cmt_date = models.DateTimeField(auto_now_add=True)


class BlogLikeModel(models.Model):

    blog_id = models.ForeignKey(BlogModel, on_delete=models.CASCADE)
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    like = models.CharField(max_length=2, default="1")
    like_date = models.DateTimeField(auto_now_add=True)