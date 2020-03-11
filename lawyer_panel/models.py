from django.db import models


class LawyerModel(models.Model):
    gender_types = (
        ("Male", "Male"),
        ("Female", "Female")
    )

    def upload_profile_image(self, filename):
        path = f"lawyer_panel/user_profile/{filename}"
        return path

    full_name = models.CharField(max_length=200, blank=False, null=False)
    speciality = models.CharField(max_length=200)
    contact = models.IntegerField(blank=False, null=False)
    email = models.EmailField(unique=True)
    password = models.CharField(default="123", max_length=200, blank=False, null=False)
    address = models.TextField()
    gender = models.CharField(max_length=20, choices=gender_types, blank=False, null=False)
    birth_date = models.DateField()
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    pincode = models.IntegerField(null=True, blank=True)
    profile_image = models.ImageField(upload_to=upload_profile_image, blank=False, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
