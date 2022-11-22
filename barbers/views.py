from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from orders.models import Order

from .models import Barber


@login_required(login_url="index_login")
def barber_dashboard(request):
    barbers = Barber.objects.order_by("-id")
    paginator = Paginator(barbers, 30)
    page = request.GET.get("page")
    barbers_per_page = paginator.get_page(page)
    package = {"barbers": barbers_per_page}
    return render(request, "barbers/barber_dashboard.html", package)


@login_required(login_url="index_login")
def get_barber(request, barber_id):
    barber = get_object_or_404(Barber, pk=barber_id)
    orders = Order.objects.order_by("-id").filter(barber=barber_id)
    total_orders = 0
    for order in orders:
        total_orders += 1
    package = {"barber": barber, "orders": orders, "total_orders": total_orders}
    return render(request, "barbers/get_barber.html", package)


@login_required(login_url="index_login")
def create_barber(request):
    if request.method == "POST":
        barber_name = request.POST["barber_name"]
        barber_cpf = request.POST["barber_cpf"]
        barber = Barber.objects.create(name=barber_name, cpf=barber_cpf)
        barber.save()
        return redirect("barber_dashboard")
    else:
        return render(request, "barbers/create_barber.html")


@login_required(login_url="index_login")
def delete_barber(request, barber_id):
    barber = get_object_or_404(Barber, pk=barber_id)
    barber.delete()
    return redirect("barber_dashboard")


@login_required(login_url="index_login")
def edit_barber(request, barber_id):
    barber = get_object_or_404(Barber, pk=barber_id)
    barber_to_edit = {"barber": barber}
    return render(request, "barbers/edit_barber.html", barber_to_edit)


@login_required(login_url="index_login")
def update_barber(request):
    if request.method == "POST":
        barber_id = request.POST["barber_id"]
        barber = Barber.objects.get(pk=barber_id)
        barber.name = request.POST["barber_name"]
        barber.cpf = request.POST["barber_cpf"]
        barber.save()
    return redirect("barber_dashboard")
