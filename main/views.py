from django.shortcuts import get_object_or_404, render
from django.http import Http404

from .models import Student

def index(request):
    student_list = Student.objects.all()
    context = {'student_list': student_list}
    return render(request, 'index.html', context)

def detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'person.html', {'student': student})
