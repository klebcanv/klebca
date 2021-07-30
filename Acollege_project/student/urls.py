from django.urls import path
from . import views

urlpatterns = [
    path('attandance/',views.attandance,name='attandance'),
    path('performance/',views.performance,name='performance'),
    path('task/',views.task.as_view(),name='task'),
    # path('at_form/<slug:username>/',views.at_form,name='at_form'),
]