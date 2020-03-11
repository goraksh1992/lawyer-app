from django.db import models
from lawyer_panel.models import LawyerModel
from datetime import datetime


class UserModel(models.Model):
    gender_types = (
        ("Male", "Male"),
        ("Female", "Female")
    )

    def upload_profile_image(self, filename):
        path = f"user/user_profile/{filename}"
        return path

    full_name = models.CharField(max_length=200, blank=False, null=False)
    contact = models.IntegerField(blank=False, null=False)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200, blank=False, null=False)
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


class AppointmentsModel(models.Model):

    status = (
        ('0', 'waiting'),
        ('1', 'accept'),
        ('2', 'reject')
    )

    lawyer_id = models.ForeignKey(LawyerModel, on_delete=models.CASCADE)
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    app_date = models.DateField()
    app_time = models.TimeField()
    app_desc = models.TextField()
    app_status = models.CharField(max_length=20, default='0', choices=status)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.app_desc


class LawyerFeedback(models.Model):

    lawyer_id = models.OneToOneField(LawyerModel, on_delete=models.CASCADE)
    user_id = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    message = models.TextField()
    rating = models.FloatField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

