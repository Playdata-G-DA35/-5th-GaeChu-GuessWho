from django.urls import path
from . import views

app_name = 'poll'

urlpatterns = [
    path("cat_list", views.cat_list, name="cat_list"),
    path("img_list/<int:category_id>", views.img_list, name="img_list"),
    path("ans_vote/<str:img_name>", views.ans_vote, name="ans_vote")
]