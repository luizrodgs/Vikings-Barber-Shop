from django.shortcuts import render


# Create your views here.
def service_dashboard(request):
    return render(request, "services.html")


def create_service(request):
    return render(request, "index.html")
