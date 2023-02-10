from django.shortcuts import render

def index(request):
    template_name = ''
    carros = Carro.objects.all()
    context = {
        'carros': carros
    }
    render(request, template_name, context)