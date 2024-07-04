from django.urls import path
from . import views

app_name = 'poll'

urlpatterns = [
    path("hello", views.hello, name="hello_poll"),
    path("list", views.list, name="list"),
    path("vote_form/<int:question_id>", views.vote_form, name="img_list"),
]