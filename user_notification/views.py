from django.shortcuts import render, redirect
from user_notification.models import JobAlert
from . import forms


def notification(request):
    if request.method == 'POST':
        form = forms.CreateJobAlert(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    else:
        form = forms.CreateJobAlert()
    return render(request, 'user_notification/notification.html', {'form': form})


def show_details(request):
    user_form = JobAlert.check_if_alert_exist("Vardit")
    if user_form == "Job Alert Not Exist":
        return render(request, 'user_notification/notification.html', {'form': user_form})
    return render(request, 'user_notification/show_details.html', {})
