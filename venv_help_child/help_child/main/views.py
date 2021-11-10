from django.shortcuts import render
from django.views import generic
# Create your views h

class IndexView(gneric.TemplateView):
    template_name="index.html"