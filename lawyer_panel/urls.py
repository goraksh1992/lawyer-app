from django.urls import path
from .views import (
    get_lawyer_appointments,
    lawyer_login,
    get_lawyer_appointment_details,
    get_lawyer_profile,
    reschedule_appointment,
    update_lawyer_details,
    accept_reject_appointment,
    get_lawyer_details
)

urlpatterns = [

    path('get-lawyer-appointments/<int:lawyer_id>', get_lawyer_appointments, name="get-lawyer-appointments"),
    path('lawyer-login', lawyer_login, name="lawyer_login"),
    path('get-lawyer-appointment-details/<int:id>', get_lawyer_appointment_details, name="get-lawyer-appointment-details"),
    path('get-lawyer-profile/<int:id>', get_lawyer_profile, name="get-lawyer-profile"),
    path('reschedule-appointment/<int:id>', reschedule_appointment, name="reschedule-appointment"),
    path('update-lawyer-details/<int:id>', update_lawyer_details, name="update-lawyer-details"),
    path('accept-reject-appointment/<int:id>', accept_reject_appointment, name="accept-reject-appointment"),
    path('get-lawyer-details', get_lawyer_details, name="get-lawyer-details"),
]