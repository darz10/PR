from .views import ImpressionList
from django.urls import path

urlpatterns = [
    path('', ImpressionList.as_view(), name='list_places_remember'),
]
