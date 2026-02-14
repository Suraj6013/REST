from django.urls import path, include
from . import views

urlpatterns = [
    path('employees/', views.EmployeeListCreate.as_view(), name='employee-list-create'),

]