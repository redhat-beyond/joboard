from django.conf.urls import url
from . import views
from joboard_home import views as home_views


app_name = 'accounts'


urlpatterns = [
    url('signup/', views.sign_up_view, name='signup'),
    url('account/', views.account_view, name='account'),
    url('home/', home_views.home_page, name='home'),
]
