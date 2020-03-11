from django.db import models


class PostModel(models.Model):

    status = (
        ("0", "Hold"),
        ("1", "Publish"),
    )

    def upload_image(self, filename):
        path = f"post/post_image/{filename}"
        return path

    post_title = models.CharField(max_length=500, blank=False, null=False)
    post_description = models.TextField(blank=False, null=False)
    post_image = models.ImageField(upload_to=upload_image, blank=False, null=False)
    writer_name = models.CharField(max_length=200, blank=False, null=False)
    post_status = models.CharField(max_length=50, choices=status)
    post_date = models.DateTimeField(auto_now_add=True)
    like_count = models.IntegerField()
    comment_count = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post_title
