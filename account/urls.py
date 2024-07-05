from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

app_name = "account"
urlpatterns = [
    path("join", views.create, name='join'),
    path("login", LoginView.as_view(template_name="account/login.html", form_class=AuthenticationForm), name='login'),
]