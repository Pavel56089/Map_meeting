from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404

from .models import Student
from .forms import StudentForm

def index(request):
    student_list = Student.objects.all()
    context = {'student_list': student_list}
    return render(request, 'index.html', context)

def detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'person.html', {'student': student})

def add(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return redirect('detail', student_id=student.id)
    else:
        form = StudentForm()
    return render(request, 'add.html', {'form': form})
