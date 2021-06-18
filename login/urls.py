from login.views import sign_in
from django.urls import path


urlpatterns = [
    path('', sign_in, name='sign_in'),
]
