from django.urls import path
from .views import GetSubscriptionDetails

urlpatterns = [

    path('get-subscription-details', GetSubscriptionDetails.as_view(), name="get-subscription-details"),
]