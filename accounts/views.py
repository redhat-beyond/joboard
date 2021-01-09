from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserAccount
from django.contrib.auth.views import LoginView as BaseLogin
from django.shortcuts import render, redirect
from django.views.generic import View, FormView
from .forms import SignUpForm, UserForm, AccountForm


class LoginExcluded(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user is not None and request.user.is_authenticated:
            return redirect('home_page')
        return super().dispatch(request, *args, **kwargs)


class SignUpView(FormView, LoginExcluded):
    model = User
    form_class = SignUpForm
    template_name = 'signup.html'

    # noinspection PyAttributeOutsideInit
    def post(self, request, *args, **kwargs):
        self.form = self.get_form()
        form = super(SignUpView, self).get_form(self.form_class)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            request = self.request
            request.user = user
            login(request, request.user)
            return redirect('home_page')
        return render(request, self.template_name)


class LoginView(BaseLogin, LoginExcluded):
    template_name = 'registration/login.html'


@login_required
def account_view(request):
    return render(request, 'account.html')


@login_required
def user_update(request):
    account = UserAccount.objects.get(user=request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        account_form = AccountForm(request.POST, instance=account)
        if user_form.is_valid() and account_form.is_valid():
            request.user = user_form.save()
            account = account_form.save()
            messages.success(request, 'User details updated.')

    else:
        user_form = UserForm()
        account_form = AccountForm()
    return render(request, 'profile.html', {'user_form': user_form, 'account_form': account_form})
