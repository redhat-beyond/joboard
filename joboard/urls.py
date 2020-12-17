from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from joboard_home import views
from accounts import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^notification/', include('user_notification.urls')),
    path('', views.home_page, name='home_page'),
    path('accounts/', include('accounts.urls')),
    path('signup/', user_views.signup_view, name='signup'),
    path('login/', user_views.login_view, name='login'),
]
