from django.conf.urls import url
from django.urls import path
from . import views
from joboard_home import views as home_views


app_name = 'accounts'


urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    url('account/', views.account_view, name='account'),
    url('home/', home_views.home_page, name='home'),
    path('login/', views.LoginView.as_view(), name='login'),
]
