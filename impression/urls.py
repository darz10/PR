from .views import creating_impression
from .views import ImpressionList 
from django.urls import path

urlpatterns = [
    path('', ImpressionList.as_view(), name='list_places_remember'),
    path('create_impression/', creating_impression, name='create_impression'),
]
