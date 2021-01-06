from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


def sign_up_view(request):
    if request.user.is_authenticated:
        return redirect('home_page')
    if request.method == 'POST':
        registration_form = SignUpForm(request.POST)
        if registration_form.is_valid():
            user = registration_form.save()
            user.save()
            login(request, user)
            return redirect('home_page')
    else:
        registration_form = SignUpForm()

    return render(request, 'signup.html', {'registration_form': registration_form})


@login_required(login_url='/login')
def account_view(request):
    return render(request, 'account.html')
