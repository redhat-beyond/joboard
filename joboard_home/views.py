from django.shortcuts import render
from user_notification.models import JobAlert


def home_page(request):
    return render(request, 'joboard_home/home_page.html')


def show_details(request):
    user_form = JobAlert.check_if_alert_exist(request.user.username)
    return render(request, 'joboard_home/show_details.html', {'user_form': user_form})
