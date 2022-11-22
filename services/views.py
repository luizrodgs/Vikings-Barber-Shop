from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .models import Service


@login_required(login_url="index_login")
def service_dashboard(request):
    services = Service.objects.order_by("-id")
    paginator = Paginator(services, 30)
    page = request.GET.get("page")
    services_per_page = paginator.get_page(page)
    package = {"services": services_per_page}
    return render(request, "services/services_dashboard.html", package)


@login_required(login_url="index_login")
def get_service(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    service_to_show = {"service": service}
    return render(request, "services/get_service.html", service_to_show)


@login_required(login_url="index_login")
def create_service(request):
    if request.method == "POST":
        service_service = request.POST["service_service"]
        service_price = request.POST["service_price"]
        service = Service.objects.create(service=service_service, price=service_price)
        service.save()
        return redirect("service_dashboard")
    else:
        return render(request, "services/create_service.html")


@login_required(login_url="index_login")
def delete_service(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    service.delete()
    return redirect("service_dashboard")


@login_required(login_url="index_login")
def edit_service(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    service_to_edit = {"service": service}
    return render(request, "services/edit_service.html", service_to_edit)


@login_required(login_url="index_login")
def update_service(request):
    if request.method == "POST":
        service_id = request.POST["service_id"]
        service = Service.objects.get(pk=service_id)
        service.service = request.POST["service_service"]
        service.price = request.POST["service_price"]
        service.save()
    return redirect("service_dashboard")
