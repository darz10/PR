from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import Impression


class ImpressionList(LoginRequiredMixin, ListView):
    """Список имеющихся воспоминаний"""

    login_url = 'login/'
    queryset = Impression.objects.all()
    context_object_name = 'places'
    template_name = 'main.html'

    