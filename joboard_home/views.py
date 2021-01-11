from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from user_notification.models import JobAlert


def home_page(request):
    return render(request, 'joboard_home/home_page.html')


@login_required
def show_details(request):
    user_form = JobAlert.check_if_alert_exist(request.user.username)
    if user_form == "Job Alert Not Exist":
        return redirect('alertForm')
    else:
        return render(request, "user_notification/show_details.html", {'user_form': user_form})
