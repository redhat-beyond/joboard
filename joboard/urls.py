from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from joboard_home import views
from accounts import views as user_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^notification/', include('user_notification.urls')),
    path('', views.home_page, name='home_page'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', user_views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='signup/login.html'), name='login'),
    path('logout/', auth_views.LogoutView),
    url(r'^jobs/', include('searchJob.urls')),
]
