from django.urls import path

from .views import (
    create_service,
    delete_service,
    edit_service,
    get_service,
    service_dashboard,
    update_service,
)

urlpatterns = [
    path("dashboard/", service_dashboard, name="service_dashboard"),
    path("<int:service_id>", get_service, name="get_service"),
    path("adicionar/", create_service, name="create_service"),
    path("editar/<int:service_id>", edit_service, name="edit_service"),
    path("atualizar", update_service, name="update_service"),
    path("deletar/<int:service_id>", delete_service, name="delete_service"),
]
