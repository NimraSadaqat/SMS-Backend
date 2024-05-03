from django.db import models

# Create your models here.

class FamilyInformation(models.Model):
    father_name = models.CharField(max_length=100)
    father_nic_number = models.CharField(max_length=15)
    father_occupation = models.CharField(max_length=100)
    father_monthly_income = models.DecimalField(max_digits=10, decimal_places=2)
    father_qualification = models.CharField(max_length=100)
    father_address = models.TextField()
    father_phone_number = models.CharField(max_length=15)
    father_cell_number = models.CharField(max_length=15)
    father_email = models.EmailField()
    emergency_number = models.CharField(max_length=15)

    def __str__(self):
            return f"{self.father_name}"

class Student(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    place_of_birth = models.TextField()
    religion = models.CharField(max_length=50)
    nationality = models.CharField(max_length=100)
    last_school = models.TextField(null=True, blank=True)
    date_of_admission = models.DateTimeField(auto_now_add=True)
    admission_number = models.CharField(max_length=10)
    remarks = models.TextField(null=True, blank=True)
    family = models.ForeignKey(FamilyInformation, on_delete=models.PROTECT)
    
    def __str__(self):
        return f"{self.name}"

