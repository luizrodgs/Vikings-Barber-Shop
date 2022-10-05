from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .models import Client


def client_dashboard(request):
    clients = Client.objects.order_by("name")
    paginator = Paginator(clients, 30)
    page = request.GET.get("page")
    clients_per_page = paginator.get_page(page)
    package = {"clients": clients_per_page}
    return render(request, "clients/client_dashboard.html", package)


def get_client(request, client_cpf):
    client = get_object_or_404(Client, pk=client_cpf)
    client_to_show = {"client": client}
    return render(request, "clients/get_client.html", client_to_show)


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


def delete_client(request, client_cpf):
    client = get_object_or_404(Client, pk=client_cpf)
    client.delete()
    return redirect("client_dashboard")


def edit_client(request, client_cpf):
    client = get_object_or_404(Client, pk=client_cpf)
    client_to_edit = {"client": client}
    return render(request, "clients/edit_client.html", client_to_edit)


def update_client(request):
    if request.method == "POST":
        client_cpf = request.POST["client_cpf"]
        client = Client.objects.get(pk=client_cpf)
        client.name = request.POST["client_name"]
        client.cpf = request.POST["client_cpf"]
        client.phone = request.POST["client_phone"]
        client.save()
    return redirect("client_dashboard")
