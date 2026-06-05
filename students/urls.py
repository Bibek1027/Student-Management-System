from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    # path('test/', views.test),
    path('add_student/', views.add_student),
    path('update_student/<int:id>/', views.update_student),
    path('delete_student/<int:id>/', views.delete_student),
    path('signup/', views.signup),
]