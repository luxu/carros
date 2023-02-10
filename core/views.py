from django.shortcuts import render

from .models import Car


def index(request):
    template_name = 'car/index.html'
    cars = Car.objects.all()
    context = {
        'cars': cars
    }
    return render(request, template_name, context)
