from django.views.generic import ListView
from django.shortcuts import render

from .models import Student,Teacher

def students_list(request):
    template = 'school/students_list.html'
    ordering = 'group'
    object_list = Student.objects.all().order_by(ordering).prefetch_related('teacher')
    context = {'object_list': object_list}
    
    return render(request, template, context)


def list_of_teacher(request):
    template = 'school/teacher_list.html'
    object_list = Teacher.objects.all().prefetch_related('students')
    context = {'object_list': object_list}

    return render(request, template, context)
