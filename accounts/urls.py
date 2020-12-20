from django.conf.urls import url
from . import views


urlpatterns = [
    url('/signup/', views.signup_view, name="signup"),
]
