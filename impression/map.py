import folium
from geopy.geocoders import Nominatim


def creating_map():
    """Создание карты"""

    map = folium.Map(location=[56.8324, -299.4488], width=600, height=400, on_touch=True, popup='more info', zoom_start=5)
    return map
    
def getting_location(location_):
    """Получение координат из формы"""

    geolocator = Nominatim(user_agent='impression')
    location = geolocator.geocode(location_)
    l_lat = float(location.latitude)
    l_lon = float(location.longitude)
    coordinate = [l_lat, l_lon]
    return coordinate

def marking_location(coordinate):
    """Создание маркера на карте по заданным координатам"""

    map = folium.Map(width=800, height=500, on_touch=True, popup='more info', zoom_start=5)
    folium.Marker(coordinate, tooltip='click here for more', icon=folium.Icon(color='red')).add_to(map)
    return map
