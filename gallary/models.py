from django.db import models


class GalleryModel(models.Model):

    image = models.FileField(blank=False, null=False)
    image_title = models.CharField(max_length=200, blank=False, null=False)
    image_description = models.TextField()

    def __str__(self):
        return self.image.name

