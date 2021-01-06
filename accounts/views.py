from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView as BaseLogin
from django.contrib.auth.decorators import login_required
from django.views.generic import View, FormView


class LoginExcluded(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user is not None and request.user.is_authenticated:
            return redirect('home_page')
        return super().dispatch(request, *args, **kwargs)


class SignUpView(FormView, LoginExcluded):
    model = User
    form_class = SignUpForm
    template_name = 'signup.html'

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
