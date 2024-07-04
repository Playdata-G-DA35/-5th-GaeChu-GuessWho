from django.urls import path
from . import views

app_name = 'poll'

urlpatterns = [
    path("hello", views.hello, name="hello_poll"),
    path("list", views.list, name="list"),
    path("img_list/<int:question_id>", views.img_list, name="img_list"),
    path("ans_vote", views.ans_vote, name="ans_vote")
]