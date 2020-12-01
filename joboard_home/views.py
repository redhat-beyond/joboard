from django.shortcuts import render


def home_page(request):
    return render(request, 'joboard_home/home_page.html')
