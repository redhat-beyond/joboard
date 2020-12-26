from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login
from django.contrib import messages


def sign_up_view(request):
    if request.method == 'POST':
        registration_form = SignUpForm(request.POST)
        if registration_form.is_valid():
            user = registration_form.save()
            user.save()
            login(request, user)
            messages.success(request, 'Welcome to JoBoard! ')
            return redirect('/')
    else:
        registration_form = SignUpForm()

    return render(request, 'sign_up.html', {'registration_form': registration_form})
