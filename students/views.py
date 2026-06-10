from django.shortcuts import redirect, render, get_object_or_404
from .models import Student
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import StudentForm
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from django.urls import reverse_lazy

#@login_required
# def home(request): #ListView
    # search = request.GET.get('search')

    # if search: #icontains  is used to search for a substring in the name field of the Student model, ignoring case sensitivity.
    #     students = Student.objects.filter(name__icontains=search) 
    # else:
    #     students = Student.objects.all()

    # return render(request, 'home.html', {
    #     'students': students
    # })
    
class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'home.html'
    context_object_name = 'students'
    paginate_by = 5 #each page will show 5 students (pagination)
    
    def get_queryset(self):
        query = self.request.GET.get('search')
        
        if query:
            return Student.objects.filter(name__icontains=query)
        return Student.objects.all()

def about(request): 
    return render(request, 'about.html')

# @login_required
# @staff_member_required
# def add_student(request):

#     form = StudentForm()
    
#     if request.method == "POST":
#         form = StudentForm(request.POST)
        
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Student added successfully!')
#             return redirect('/')
        
#     return render(request, 'add_student.html', {
#         'form' : form 
#     })

class StudentCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Student
    fields = ['name', 'course']
    template_name = 'add_student.html'
    success_url = reverse_lazy('home') #where to go after saving
    
    def test_func(self): #Is this user allowed to access this page
        return self.request.user.is_staff 

# @login_required
# @staff_member_required
# def update_student(request, id):

#     student = get_object_or_404(Student, id=id)
    
#     form = StudentForm(instance=student)
    
#     if request.method == "POST":
#         form = StudentForm(request.POST, instance=student)
        
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Student updated successfully!')
#             return redirect('/')   
    
#     return render(request, 'update_student.html', {
#         'form' : form,
#         'student' : student
#     })

class StudentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Student
    fields = ['name', 'course']
    template_name = 'update_student.html'
    success_url = reverse_lazy('home') #where to go after saving
    
    def test_func(self): #Is this user allowed to access this page
        return self.request.user.is_staff

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

# class StudentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = Student
#     template_name = 'delete_student.html'
#     context_object_name = 'student'
#     success_url = reverse_lazy('home') #where to go after deleting

#     def test_func(self):
#         return self.request.user.is_staff
    
    
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

class StudentDetailView(LoginRequiredMixin, DetailView):
    model = Student
    template_name = 'student_detail.html'
    context_object_name = 'student'
    