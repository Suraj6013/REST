from django.urls import path, include
from . import views

urlpatterns = [
    path('employees/', views.EmployeeListCreate.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', views.EmployeeDetail.as_view(), name='employee-detail'),

]