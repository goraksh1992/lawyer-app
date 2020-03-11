from django.contrib import admin
from .models import UserModel, AppointmentsModel, LawyerFeedback

admin.site.register([UserModel, AppointmentsModel, LawyerFeedback])
