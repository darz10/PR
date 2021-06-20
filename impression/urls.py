from .views import getting_list_impression, creating_impression, updating_impression, deleting_impression,  django_logout
from django.urls import path

urlpatterns = [
    path('', getting_list_impression, name='list_places_remember'),
    path('create_impression/', creating_impression, name='create_impression'),
    path('update_impression/<int:pk>/', updating_impression, name='update_impression'),
    path('delete_impression/<int:pk>/', deleting_impression, name='delete_impression'),
    path('logout/', django_logout, name='loguot_page')

]
