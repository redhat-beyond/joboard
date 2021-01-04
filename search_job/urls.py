from django.conf.urls import url
from . import views

app_name = 'search_job'

urlpatterns = [
    url(r'^$', views.jobs),
]
