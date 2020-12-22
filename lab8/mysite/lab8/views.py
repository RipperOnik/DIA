from django.shortcuts import render
from django.http import HttpResponse
from .models import Animal
from django.template import loader
from django.http import Http404


def index(request):
    animal_list = Animal.objects.all()
    template = loader.get_template('lab8/index.html')
    context = {
        'animal_list': animal_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, id):
    try:
        animal = Animal.objects.get(pk=id)
    except Animal.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'lab8/detail.html', {'animal': animal})