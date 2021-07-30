from django.shortcuts import render
from django.views.generic.base import TemplateView
from kle_main.models import request_book
# Create your views here.
class request(TemplateView):
  template_name = 'library/request.html'
  def get_context_data(self, *args, **kwargs):
    context = super().get_context_data(**kwargs)
    stud = request_book.objects.all()
    context = {'stu':stud}
    return context