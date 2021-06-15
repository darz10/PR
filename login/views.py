from django.shortcuts import render


def sign_in(request):
    return render(request, 'account/login.html')
