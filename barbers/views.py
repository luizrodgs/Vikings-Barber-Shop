from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .models import Barber


def barber_dashboard(request):
    barbers = Barber.objects.order_by("name")
    paginator = Paginator(barbers, 30)
    page = request.GET.get("page")
    barbers_per_page = paginator.get_page(page)
    package = {"barbers": barbers_per_page}
    return render(request, "barbers/barber_dashboard.html", package)


def get_barber(request, barber_id):
    barber = get_object_or_404(barber, pk=barber_id)
    barber_to_show = {"barber": barber}
    return render(request, "barbers/get_barber.html", barber_to_show)


def create_barber(request):
    if request.method == "POST":
        barber_name = request.POST["barber_name"]
        barber_cpf = request.POST["barber_cpf"]
        barber = Barber.objects.create(name=barber_name, cpf=barber_cpf)
        barber.save()
        return redirect("barber_dashboard")
    else:
        return render(request, "barbers/create_barber.html")


def delete_barber(request, barber_id):
    barber = get_object_or_404(Barber, pk=barber_id)
    barber.delete()
    return redirect("barber_dashboard")


def edit_barber(request, barber_id):
    barber = get_object_or_404(Barber, pk=barber_id)
    barber_to_edit = {"barber": barber}
    return render(request, "barbers/edit_barber.html", barber_to_edit)


def update_barber(request):
    if request.method == "POST":
        barber_id = request.POST["barber_id"]
        barber = Barber.objects.get(pk=barber_id)
        barber.name = request.POST["barber_name"]
        barber.cpf = request.POST["barber_cpf"]
        barber.save()
    return redirect("barber_dashboard")
