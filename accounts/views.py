from django.shortcuts import render, redirect
from .forms import SignUpForm, AccountForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages


def signup_view(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        account_form = AccountForm(request.POST)
        if user_form.is_valid() and account_form.is_valid():
            user = user_form.save()
            user.save()
            user_account = account_form.save(commit=False)
            user_account.user = user
            user_account.save()
            login(request, user)
            messages.success(request, 'Welcome to JoBoard! ')
            return redirect('home_page')
    else:
        user_form = SignUpForm()
        account_form = AccountForm()

    return render(request, 'signup/signup.html', {'user_form': user_form, 'account_form': account_form})


def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            messages.success(request, 'Welcome to JoBoard! ')
            return redirect('home_page')
    else:
        login_form = AuthenticationForm()
    return render(request, 'login/login.html', {'login_form': login_form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home_page')
