
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

@api_view(['GET'])
def salary_filter(request):
    min_salary = request.GET.get('min_salary')
    if min_salary:
        employees = Employee.objects.filter(salary__gt=min_salary)
    else:
        employees = Employee.objects.all()
    data = [{'name': e.name, 'salary': e.salary} for e in employees]
    return Response(data)
