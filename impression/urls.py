from impression import sign_in
from django.urls import path
from .views import login

urlpatterns = [
    path('', sign_in, name='sign_in'),
]
