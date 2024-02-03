from django.urls import path
from .views import *

urlpatterns = [
    path('',ElderHomeView.as_view()),
    path('find-care-worker',FindCareWorkerView.as_view()),
    path('find-care-worker/<int:id>',FindCareWorkerView.as_view()),
    path('care-workers/request/<int:id>',SendHiringRequestToCareWorkerView.as_view()),
    path('book-appointment',BookAppointmentView.as_view()),
]