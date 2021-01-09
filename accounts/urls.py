from django.conf.urls import url
from django.urls import path
from . import views


app_name = 'accounts'


urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    url('account/', views.account_view, name='account'),
    path('login/', views.LoginView.as_view(), name='login'),
    url('profile/', views.user_update, name='profile'),
]
