from django.db import models

# Create your models here.

class EmployeeSalary(models.Model):
    salary = models.CharField(max_length=50)

    def __str__(self):
        return self.salary

class Employee(models.Model):
    Department_field = (
        ('Programmer', 'Programmer'),
        ('SEO', 'SEO'),
        ('HR', 'HR'),
    )
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=4)
    department = models.CharField(max_length=10, choices=Department_field)
    salary = models.ForeignKey(EmployeeSalary, on_delete=models.CASCADE)
    