from django.urls import path
from .views import *

urlpatterns = [
    path('',HwHomeView.as_view()),   
    path('hiring-requests',HwHiringReqView.as_view()),
    path('hiring-requests/accept/<int:id>',HwAcceptReqView.as_view()),
    path('hiring-requests/reject/<int:id>',HwRejectReqView.as_view()),
]