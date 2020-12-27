from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from joboard_home import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^notification/', include('user_notification.urls')),
    path('', views.home_page, name='home_page'),
    path('accounts/', include('accounts.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='log_in.html'), name='login'),
    path('logout/', auth_views.LogoutView, name='logout'),
    url(r'^jobs/', include('searchJob.urls')),
]
