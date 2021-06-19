from .views import creating_impression, updating_impression
from .views import ImpressionList, DeleteImpressionView
from django.urls import path

urlpatterns = [
    path('', ImpressionList.as_view(), name='list_places_remember'),
    path('create_impression/', creating_impression, name='create_impression'),
    path('update_impression/<int:pk>/', updating_impression, name='update_impression'),
    path('delete_impression/<int:pk>/', DeleteImpressionView.as_view(), name='delete_impression'),

]
