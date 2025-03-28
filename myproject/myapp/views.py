from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Student
from .models import Teacher
def home(request):
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    return render(request, 'home.html', {'students': students, 'teachers': teachers})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})
def student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'student_detail.html', {'student': student})
def student_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        email = request.POST['email']
        Student.objects.create(name=name, age=age, email=email)
        return redirect('student-list')
    return render(request, 'student_form.html')
def student_update(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.name = request.POST['name']
        student.age = request.POST['age']
        student.email = request.POST['email']
        student.save()
        return redirect('student-list')
    return render(request, 'student_form.html', {'student': student})
def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('student-list')
def teacher_detail(request,id):
    teacher=get_object_or_404(Teacher,id=id)
    teacher.name="shahid"
    teacher.age=23
    return render(request, 'teacher_detail.html', {'teacher': teacher})
