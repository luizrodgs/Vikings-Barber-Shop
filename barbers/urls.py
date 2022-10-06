from django.urls import path

from .views import (
    barber_dashboard,
    create_barber,
    delete_barber,
    edit_barber,
    get_barber,
    update_barber,
)

urlpatterns = [
    path("<int:barber_id>", get_barber, name="get_barber"),
    path("dashboard/", barber_dashboard, name="barber_dashboard"),
    path("cadastrar/", create_barber, name="create_barber"),
    path("editar/<int:barber_id>", edit_barber, name="edit_barber"),
    path("atualizar", update_barber, name="update_barber"),
    path("deletar/<int:barber_id>", delete_barber, name="delete_barber"),
]
