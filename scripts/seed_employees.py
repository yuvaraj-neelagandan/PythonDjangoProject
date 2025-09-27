import os
import sys
import django
import random

# STEP 1: Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# STEP 2: Set the correct settings module name
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'employee_project.settings')

# STEP 3: Setup Django
django.setup()

# STEP 4: Now safe to import Django models
from employees.models import Employee

# STEP 5: Create 100 employees
first_names = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Henry", "Ivy", "Jack"]
domains = ["example.com", "mail.com", "demo.org"]

for i in range(1, 101):
    name = random.choice(first_names) + str(i)
    email = f"user{i}@{random.choice(domains)}"
    salary = random.randint(100, 100000)
    Employee.objects.create(name=name, email=email, salary=salary)

print("100 dummy employees created.")
