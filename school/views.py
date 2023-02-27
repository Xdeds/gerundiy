from django.shortcuts import render
from school.models import Teacher, Student, Graduate, Gallery
from django.http import HttpResponseRedirect


# Create your views here.
def main(request):
    # info = Teacher.objects.all()
    return render(request, 'main.html')

def gallery(request):
    teacher = Teacher.objects.all()
    student = Student.objects.all()
    graduate = Graduate.objects.all()
    gallery = Gallery.objects.all()
    return render(request, 'gallery.html', {'teacher': teacher, 'student': student, 'graduate': graduate, 'gallery':gallery})

def table1(request):
    return render(request, 'table1.html')

def teacher(request):
    teacher = Teacher.objects.all()
    return render(request, 'teacher.html', {'teacher':teacher})

def table2(request):
    return render(request, 'table2.html')


def student(request):
    student = Student.objects.all()
    return render(request, 'student.html', {'student':student})

def graduate(request):
    graduate = Graduate.objects.all()
    return render(request, 'graduate.html', {'graduate':graduate})

def priem(request):
    return render(request, 'priem.html')
