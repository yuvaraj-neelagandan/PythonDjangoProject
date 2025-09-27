
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, salary_filter

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('salaries/', salary_filter),
]
