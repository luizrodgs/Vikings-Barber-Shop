from django.urls import path

from . import views

urlpatterns = [
    path("", views.index_login, name="index_login"),
    path("cadastro", views.create_user, name="create_user"),
    path("logout", views.logout, name="logout"),
]
