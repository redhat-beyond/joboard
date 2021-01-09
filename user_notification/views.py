from django.shortcuts import render, redirect
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
