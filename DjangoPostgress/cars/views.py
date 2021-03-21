from django.shortcuts import render
from cars.models import Car, Driver

# Create your views here.


def car_detail(request, pk):
    owner_obj = Driver.objects.get(pk=pk)
    cars_obj = Car.objects.filter(owner_id=owner_obj.id)

    context = {
        "vehicles": cars_obj,
        "drivers": owner_obj,
    }

    return render(request, "car_detail.html", context)
