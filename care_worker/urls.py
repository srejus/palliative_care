from django.urls import path
from .views import *

urlpatterns = [
    path('',CareWorkerView.as_view(),name='care_worker_home'),
    path('hiring-requests',CwhiringReqView.as_view()),
    path('emergency-requests',CwEmergencyReqView.as_view()),
    path('hiring-requests/accept/<int:id>',CwAcceptReqView.as_view()),
    path('hiring-requests/reject/<int:id>',CwRejectReqView.as_view()),
]
