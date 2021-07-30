from django.urls import path
from . import views

urlpatterns = [
    path('contact_requests/',views.contact_request.as_view(),name='contact_request'),
    path('feedback/',views.home_all_feedback.as_view(),name='all_feedback'),
    path('student_feedback/',views.student_feedback,name='student_feedback'),
    path('parents_feedback/',views.parents_feedback,name='parents_feedback'),
    path('staff_feedback/',views.staff_feedback,name='staff_feedback'),
]