from django.shortcuts import render
# , redirect
from .forms import SignUpForm, AccountForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
# from django.contrib.auth.decorators import login_required


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, prefix='register')
        if form.is_valid():
            user = form.save()
            user.UserAccount = AccountForm(request.POST, prefix='account')
            login(request, user)
            # messages.success(request, 'Welcome to JoBoard! ' )
            # return redirect('')
        # else:
            # messages.error(request, 'Unsuccessful registration ')

    else:
        form = SignUpForm(request.POST, prefix='register')
    return render(request, 'templates/signup/signup.html', {'Create an account': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
#       if 'next' in request.POST:
#           return redirect(request.POST.get('next'))
#       else
#           return redirect('')

    else:
        form = AuthenticationForm()
    return render(request, 'templates/login/login.html', {'Log in': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
#       return redirect('joboard_home')
