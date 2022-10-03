from django.urls import path

from .views import *

urlpatterns = [
    path("dashboard/", service_dashboard, name="service_dashboard"),
    path("adicionar/", create_service, name="create_service"),
]
