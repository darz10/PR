from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Impression
from login.models import Profile
from .forms import ImpressionForm
from geopy.geocoders import Nominatim
import folium
from allauth.socialaccount.models import SocialAccount


def getting_socialaccount_photo(request):
    """Получение фотографии из социальной сети с помощью которой авторизовался пользователь """

    extra = SocialAccount.objects.get(user=request.user)
    photo = extra.extra_data['photo_big']
    return photo


class ImpressionList(LoginRequiredMixin, ListView):
    """Список имеющихся воспоминаний"""

    def get(self, request):
        try:
           photo = getting_socialaccount_photo(request)
        except SocialAccount.DoesNotExist:
            return redirect('login/')
        queryset = Impression.objects.filter(user=request.user)
        context = {
            'places': queryset, 
            'photo':photo
        }
        return render(request, 'main.html', context)


def creating_impression(request):
    """Создание воспоминания"""

    map = folium.Map(location=[56.8324, -299.4488], width=600, height=400, on_touch=True, popup='more info', zoom_start=5)
    geolocator = Nominatim(user_agent='impression')
    form = ImpressionForm()
    location = None

    if request.method == "POST":
        form = ImpressionForm(request.POST)
        if form.is_valid:
            response = form.save(commit=False)
            response.user = request.user
            location_ = form.cleaned_data.get('location')
            location = geolocator.geocode(location_)
            print(location)
            l_lat = float(location.latitude)
            l_lon = float(location.longitude)        
            map = folium.Map(location=[56.8324, -299.4488], width=800, height=500, on_touch=True, popup='more info', zoom_start=5)
            folium.Marker([l_lat, l_lon], tooltip='click here for more', icon=folium.Icon(color='red')).add_to(map)
            response.location = location
            # response.save()
        #return redirect('create_impression')
    map = map._repr_html_()
    context = {
        'map':map,
        'form':form,
        'location':location
    }
    return render(request, 'create_impression.html', context)




"""
folium.ClickForMarker(popup='Waypoint').add_to(map)
folium.LatLngPopup().add_to(map)
"""
