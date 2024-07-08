from django.urls import path
from . import views

app_name = 'poll'

urlpatterns = [
    path("cat_list", views.cat_list, name="cat_list"),
    path("img_list/cat<int:category_id>", views.img_list, name="img_list"),
    path("ans_vote/cat<int:category_id>/<str:img_name>", views.ans_vote, name="ans_vote"),
    path("ans_create/cat<int:category_id>/<str:img_name>", views.ans_create, name="ans_create"),
]