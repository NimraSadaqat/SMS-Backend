from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class EmployeeInformation(models.Model):
    
    CURRENT = 'current'
    LEFT = 'left'

    EmployeeStatus = [
        (CURRENT, 'Current'),
        (LEFT, 'Left')
    ]
    
    name = models.CharField(max_length=100)
    nic_number = models.CharField(max_length=15)
    qualification = models.TextField()
    address = models.TextField()
    cell_number = models.CharField(max_length=12)
    status = models.CharField(
        max_length = 7,
        choices = EmployeeStatus,
        default = CURRENT
    )
    phone_number1 = models.CharField(
         max_length = 12, 
         null = True, 
         blank = True
    )
    email = models.EmailField(
         null = True, 
         blank = True
    )
    phone_number2 = models.CharField(
         max_length = 12, 
         null = True, 
         blank = True
    )
    emergency_number = models.CharField(
         max_length = 15,
         null = True, 
         blank = True
    )
    joined_at = models.DateField(auto_now = True)
    
    def __str__(self):
            return f"{self.name}"

class Salary(models.Model):
      employee = models.ForeignKey(
            EmployeeInformation, 
            on_delete = models.CASCADE
        )
      salary = models.IntegerField(
            validators=[MinValueValidator(0), 
                     MaxValueValidator(1000000)]
      )
      absents = models.IntegerField(
            validators=[MinValueValidator(0), 
                     MaxValueValidator(31)],
            default = 0
      )
      late_commings = models.IntegerField(
            validators=[MinValueValidator(0), 
                     MaxValueValidator(31)],
            default = 0
      )
      date = models.DateField(auto_now_add = True)

      def __str__(self):
            return f"{self.employee.name}: {self.salary}"
