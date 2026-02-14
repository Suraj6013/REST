from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'employees', views.EmployeeViewSet)

urlpatterns = [
    # path('employees/', views.EmployeeListCreate.as_view(), name='employee-list-create'),
    path('', include(router.urls)),
]