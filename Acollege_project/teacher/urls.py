from django.urls import path
from . import views

urlpatterns = [
    path('attandance_update/',views.attandance_update.as_view(),name='attandance_update'),
    path('at_form/<slug:username>/',views.at_form,name='at_form'),
    path('performance_update/',views.performance_update.as_view(),name='performance_update'),
    path('per_form/<slug:username>/',views.per_form,name='per_form'),
    path('task_update/',views.task_update.as_view(),name='task_update'),
]