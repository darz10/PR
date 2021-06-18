from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Impression
from .forms import ImpressionForm
import folium
import folium.plugins.mouse_position



class ImpressionList(LoginRequiredMixin, ListView):
    """Список имеющихся воспоминаний"""

    login_url = 'login/'
    queryset = Impression.objects.all()
    context_object_name = 'places'
    template_name = 'main.html'    


def creating_impression(request):
    """Создание воспоминания"""

    form = ImpressionForm()
    map = folium.Map(width=800, height=500, on_touch=True, popup='more info', zoom_start=7)
    t = folium.LatLngPopup().add_to(map)
    print(t.to_json.__dict__)
    map = map._repr_html_()
    if request.method == "POST":
        form = ImpressionForm(request.POST)
        if form.is_valid:
            response = form.save(commit=False)
            response.user = request.user
            response.save()
        return redirect('list_places_remember')
    context = {
        'map':map,
        'form':form}
    return render(request, 'create_impression.html', context)


"""
folium.ClickForMarker(popup='Waypoint').add_to(map)
folium.LatLngPopup().add_to(map)
"""
