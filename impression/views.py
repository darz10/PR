from .models import Impression
from .forms import ImpressionForm
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from allauth.socialaccount.models import SocialAccount
from .map import creating_map, getting_location, marking_location


def getting_socialaccount_photo(request):
    """Получение фотографии из социальной сети с помощью которой авторизовался пользователь """

    try:
        extra = SocialAccount.objects.get(user=request.user)
        photo = extra.extra_data['photo_big']
    except KeyError:
        photo = None
    return photo

@login_required(login_url='sign_in')
def getting_list_impression(request):
    """Список всех впечатлений"""

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


@login_required(login_url='sign_in')
def creating_impression(request):
    """Создание воспоминания"""

    map = creating_map()
    form = ImpressionForm()
    location = None

    if request.method == "POST":
        form = ImpressionForm(request.POST)
        if form.is_valid:
            response = form.save(commit=False)
            response.user = request.user
            location_ = form.cleaned_data.get('location')
            location = getting_location(location_)
            map = marking_location(location)
            response.save()
    map = map._repr_html_()
    context = {
        'map':map,
        'form':form,
        'location':location
    }
    return render(request, 'create_impression.html', context)


@login_required(login_url='sign_in')
def updating_impression(request, pk):
    """Изменение существующих записей"""

    data = Impression.objects.get(id=pk)
    adress = data.location
    map = creating_map()
    coordinate = getting_location(adress)
    form = ImpressionForm(instance=data)
    map = marking_location(coordinate)
    if request.method == 'POST':
        form = ImpressionForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('list_places_remember')
    map = map._repr_html_()
    context = {
        'form':form,
        'map':map,
    }
    return render(request, 'update_impression.html', context)   

    
@login_required(login_url='sign_in')
def deleting_impression(request, pk):
    """Удаление выбранной записи"""

    data = Impression.objects.get(id=pk)
    if request.method == "POST":
        data.delete()
        return redirect('list_places_remember')
    return render(request, 'delete_impression.html', {'place':data})



@login_required(login_url='sign_in')
def django_logout(request):
    """Выход из аккунта"""

    logout(request)
    return redirect('sign_in')