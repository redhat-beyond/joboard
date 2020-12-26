from django.conf.urls import url
from . import views


app_name = 'accounts'


urlpatterns = [
    url('templates/', views.sign_up_view, name='sign_up'),
]
