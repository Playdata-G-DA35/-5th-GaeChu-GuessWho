from django.urls import path
from . import views

app_name = 'poll'

urlpatterns = [
    path("list", views.list, name="list"),
    path("img_list/<int:category_id>", views.img_list, name="img_list"),
    path("ans_vote/<int:img_id>", views.ans_vote, name="ans_vote")
]