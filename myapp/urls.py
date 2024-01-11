from django.urls import path
from .views import create_user, user_list, main_page

app_name = "myapp"

urlpatterns = [
    path("", main_page, name="main_page"),
    path("create_user/", create_user, name="create_user"),
    path("user_list/", user_list, name="user_list"),
]
