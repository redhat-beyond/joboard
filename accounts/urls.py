from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url('signup/', views.signup_view, name="signup"),
    url('login/', views.login_view, name="login"),
    path('', views.logout_view, name="logout"),
]
