from django.urls import path
from .views import userRegistration, updateUserDetails, add_lawyer_feedback, add_lawyer_appointment

urlpatterns = [
    path('user-registration', userRegistration, name="user-registration"),
    path('update-user-registration/<int:user_id>', updateUserDetails, name="update-user-registration"),
    path('add-feedback', add_lawyer_feedback, name="add-feedback"),
    path('add-lawyer-appointment', add_lawyer_appointment, name="lawyer-appointment")
]
