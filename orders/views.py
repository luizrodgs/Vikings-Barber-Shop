from multiprocessing.connection import Client

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .models import Barber, Client, Order, Service


@login_required(login_url="index_login")
def order_dashboard(request):
    orders = Order.objects.order_by("-id")
    paginator = Paginator(orders, 30)
    page = request.GET.get("page")
    orders_per_page = paginator.get_page(page)
    package = {"orders": orders_per_page}
    return render(request, "orders/order_dashboard.html", package)


@login_required(login_url="index_login")
def get_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    order_to_show = {"order": order}
    return render(request, "orders/get_order.html", order_to_show)


@login_required(login_url="index_login")
def create_order(request):
    if request.method == "POST":
        order_client = get_object_or_404(Client, pk=request.POST["client"])
        order_barber = get_object_or_404(Barber, pk=request.POST["barber"])
        order_service = get_object_or_404(Service, pk=request.POST["service"])
        order = Order.objects.create(
            client=order_client, barber=order_barber, service=order_service
        )
        order.save()
        return redirect("order_dashboard")
    else:
        clients = Client.objects.all()
        barbers = Barber.objects.all()
        services = Service.objects.all()
        package = {"clients": clients, "barbers": barbers, "services": services}
        return render(request, "orders/create_order.html", package)


@login_required(login_url="index_login")
def delete_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    order.delete()
    return redirect("order_dashboard")


@login_required(login_url="index_login")
def edit_order(request, order_id):
    clients = Client.objects.all()
    barbers = Barber.objects.all()
    services = Service.objects.all()
    package = {"clients": clients, "barbers": barbers, "services": services}
    return render(request, "orders/edit_order.html", package)


@login_required(login_url="index_login")
def update_order(request):
    if request.method == "POST":
        order_id = request.POST["order_id"]
        order = Order.objects.get(pk=order_id)
        order.client = request.POST["order_client"]
        order.barber = request.POST["order_barber"]
        order.service = request.POST["order_service"]
        order.save()
    return redirect("order_dashboard")
