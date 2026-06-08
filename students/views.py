#from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import Student
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import StudentForm
from django.contrib.admin.views.decorators import staff_member_required

@login_required
def home(request):

    search = request.GET.get('search')

    if search: #icontains  is used to search for a substring in the name field of the Student model, ignoring case sensitivity.
        students = Student.objects.filter(name__icontains=search) 
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
@staff_member_required
def add_student(request):

    form = StudentForm()
    
    if request.method == "POST":
        form = StudentForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Student added successfully!')
            return redirect('/')
        
    return render(request, 'add_student.html', {
        'form' : form 
    })
    
@login_required
@staff_member_required
def update_student(request, id):

    student = get_object_or_404(Student, id=id)
    
    form = StudentForm(instance=student)
    
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Student updated successfully!')
            return redirect('/')   
    
    return render(request, 'update_student.html', {
        'form' : form,
        'student' : student
    })

@login_required
@staff_member_required
def delete_student(request, id):

    student = get_object_or_404(Student, id=id)
    
    if request.method == "POST":
        student.delete()
        messages.success(request, 'Student deleted successfully!')
        return redirect('/')
    
    return render(request, 'delete_student.html', {
        'student' : student
    })

def signup(request):
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('/accounts/login/')

    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})