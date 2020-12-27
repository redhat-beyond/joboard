from django.conf.urls import url
from . import views

app_name = 'searchJob'

urlpatterns = [
    url(r'^$', views.jobs),
]
