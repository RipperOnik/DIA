from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Group, Discipline, Schedule
from django.template import loader


def index(request):
    schedule_list = Schedule.objects.all()
    group_list = Group.objects.all()
    template = loader.get_template('dz/index.html')
    context = {
        'schedule_list': schedule_list,
        'group_list': group_list,
    }
    return HttpResponse(template.render(context, request))


def k1(request):

    student_list = Student.objects.all()
    group_list = Group.objects.all()
    discipline_list = Discipline.objects.all()
    template = loader.get_template('dz/k1.html')
    context = {
        'student_list': student_list,
        'group_list': group_list,
        'discipline_list': discipline_list
    }
    return HttpResponse(template.render(context, request))


def k2(request):

    student_list = Student.objects.all()
    group_list = Group.objects.all()
    discipline_list = Discipline.objects.all()
    template = loader.get_template('dz/k2.html')
    context = {
        'student_list': student_list,
        'group_list': group_list,
        'discipline_list': discipline_list
    }
    return HttpResponse(template.render(context, request))


def g1(request):

    student_list = Student.objects.all()
    group_list = Group.objects.all()
    discipline_list = Discipline.objects.all()
    template = loader.get_template('dz/g1.html')
    context = {
        'student_list': student_list,
        'group_list': group_list,
        'discipline_list': discipline_list
    }
    return HttpResponse(template.render(context, request))