from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .models import Order


def order_dashboard(request):
    orders = Order.objects.order_by("client")
    paginator = Paginator(orders, 30)
    page = request.GET.get("page")
    orders_per_page = paginator.get_page(page)
    package = {"orders": orders_per_page}
    return render(request, "orders/order_dashboard.html", package)


def get_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    order_to_show = {"order": order}
    return render(request, "orders/get_order.html", order_to_show)


def create_order(request):
    if request.method == "POST":
        order_client = request.POST["order_client"]
        order_barber = request.POST["order_barber"]
        order_service = request.POST["order_service"]
        order = Order.objects.create(
            client=order_client, barber=order_barber, service=order_service
        )
        order.save()
        return redirect("order_dashboard")
    else:
        return render(request, "orders/create_order.html")


def delete_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    order.delete()
    return redirect("order_dashboard")


def edit_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    order_to_edit = {"order": order}
    return render(request, "orders/edit_order.html", order_to_edit)


def update_order(request):
    if request.method == "POST":
        order_id = request.POST["order_id"]
        order = Order.objects.get(pk=order_id)
        order.client = request.POST["order_client"]
        order.barber = request.POST["order_barber"]
        order.service = request.POST["order_service"]
        order.save()
    return redirect("order_dashboard")
