from functools import total_ordering

from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from orders.models import Order

from .models import Client


def client_dashboard(request):
    clients = Client.objects.order_by("name")
    paginator = Paginator(clients, 30)
    page = request.GET.get("page")
    clients_per_page = paginator.get_page(page)
    package = {"clients": clients_per_page}
    return render(request, "clients/client_dashboard.html", package)


def get_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    client_id = client.id
    orders = Order.objects.filter(client=client_id)
    total_orders = 0
    for order in orders:
        total_orders += 1
    package = {"client": client, "orders": orders, "total_orders": total_orders}
    return render(request, "clients/get_client.html", package)


def create_client(request):
    if request.method == "POST":
        client_name = request.POST["client_name"]
        client_cpf = request.POST["client_cpf"]
        client_phone = request.POST["client_phone"]
        client = Client.objects.create(
            name=client_name, cpf=client_cpf, phone=client_phone
        )
        client.save()
        return redirect("client_dashboard")
    else:
        return render(request, "clients/create_client.html")


def delete_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    client.delete()
    return redirect("client_dashboard")


def edit_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    client_to_edit = {"client": client}
    return render(request, "clients/edit_client.html", client_to_edit)


def update_client(request):
    if request.method == "POST":
        client_id = request.POST["client_id"]
        client = Client.objects.get(pk=client_id)
        client.name = request.POST["client_name"]
        client.cpf = request.POST["client_cpf"]
        client.phone = request.POST["client_phone"]
        client.save()
    return redirect("client_dashboard")
