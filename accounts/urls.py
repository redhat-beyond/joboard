from django.conf.urls import url
from . import views


app_name = 'accounts'


urlpatterns = [
    url('signup/', views.sign_up_view, name='signup'),
    url('account/', views.account_view, name='account'),
]
