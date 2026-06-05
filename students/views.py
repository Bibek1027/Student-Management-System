#from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Student
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

@login_required
def home(request):

    search = request.GET.get('search')

    if search:
        students = Student.objects.filter(name=search)
    else:
        students = Student.objects.all()

    return render(request, 'home.html', {
        'students': students
    })

def about(request):
    return render(request, 'about.html')

# def test(request):
#     return HttpResponse(request.method)

@login_required
def add_student(request):
    if not request.user.is_superuser:
        return redirect('/')

    if request.method == 'POST':
        name = request.POST.get('name')
        course = request.POST.get('course')
        
        Student.objects.create(
            name=name,
            course=course
        )
        
        messages.success(request, "Student added successfully!")

        
    return render(request, 'add_student.html')

@login_required
def update_student(request, id):
    if not request.user.is_superuser:
        return redirect('/')
    
    student = Student.objects.get(id=id)
    
    if request.method == "POST":

        student.name = request.POST.get('name')
        student.course = request.POST.get('course')

        student.save()
        
        messages.success(request, "Student updated successfully!")
        
    return render(request, 'update_student.html', {
        'student': student
        })

@login_required
def delete_student(request, id):
    if not request.user.is_superuser:
        return redirect('/')

    student = Student.objects.get(id=id)
    student.delete()
    
    messages.success(request, "Student deleted successfully!")
    
    return redirect('/')

def signup(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/accounts/login/')

    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})