from django.urls import path
from .views import *

urlpatterns = [
    path('emergency',EmergencyView.as_view()),
]