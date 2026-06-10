from django.urls import path
from . import views

urlpatterns = [
    #path('', views.home),
    path('', views.StudentListView.as_view(), name='home'),
    path('about/', views.about),
    #path('add_student/', views.add_student),
    path('add_student/', views.StudentCreateView.as_view(), name='add_student'),
    # path('update_student/<int:id>/', views.update_student),
    path('update_student/<int:pk>/', views.StudentUpdateView.as_view(), name='update_student'),
    path('delete_student/<int:id>/', views.delete_student),
    # path('delete_student/<int:pk>/', views.StudentDeleteView.as_view(), name='delete_student'),
    path('signup/', views.signup),
    path('student/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail')
]