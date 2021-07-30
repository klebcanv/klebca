from django.urls import path
from . import views

urlpatterns = [
    path('requests/',views.request.as_view(),name='request'),
]