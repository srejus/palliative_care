from django.urls import path
from .views import *

urlpatterns = [
    path('',HwHomeView.as_view()),   
    path('hiring-requests',HwHiringReqView.as_view()),
    path('hiring-requests/accept/<int:id>',HwAcceptReqView.as_view()),
    path('hiring-requests/reject/<int:id>',HwRejectReqView.as_view()),
    path('manage-emergency',HwManageEmergencyView.as_view()),
    path('manage-health-report',HwManageHealthReportView.as_view()),
    path('manage-health-report/add',HwAddHealthReportView.as_view()),
    path('delete-record/<int:id>',HwDeleteRecordView.as_view()),
]