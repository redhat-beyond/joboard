from django.conf.urls import url
from . import views

app_name = 'user_notification'

urlpatterns = [
    url(r'^$', views.notification),
    url(r'^$', views.show_details),
]
