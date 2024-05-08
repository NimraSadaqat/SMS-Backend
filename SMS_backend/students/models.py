from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
from academic_year.models import Academic_Year

# Create your models here.

class FamilyInformation(models.Model):
    
    CURRENT = 'current'
    LEFT = 'left'

    FamilyStatus = [
        (CURRENT, 'Current'),
        (LEFT, 'Left')
    ]
    
    father_name = models.CharField(max_length=100)
    father_nic_number = models.CharField(max_length=15)
    father_occupation = models.CharField(max_length=100)
    father_monthly_income = models.IntegerField(
         validators=[MinValueValidator(1000), 
                     MaxValueValidator(1000000)]
    )
    father_qualification = models.CharField(max_length=100)
    father_address = models.TextField()
    father_cell_number = models.CharField(max_length=12)
    status = models.CharField(
        max_length = 7,
        choices = FamilyStatus,
        default = CURRENT
    )
    father_phone_number = models.CharField(
         max_length=12, 
         null=True, 
         blank=True
    )
    father_email = models.EmailField(
         null=True, 
         blank=True
    )
    father_office_address = models.TextField(
         null=True, 
         blank=True
    )
    father_office_number = models.CharField(
         max_length=12, 
         null=True, 
         blank=True
    )
    mother_name = models.CharField(max_length=100)
    mother_nic_number = models.CharField(max_length=15)
    mother_occupation = models.CharField(
         max_length=100,
         null=True, 
         blank=True
    )
    mother_monthly_income = models.IntegerField(
         validators=[MinValueValidator(1000), 
                     MaxValueValidator(1000000)],
         null=True, 
         blank=True
    )
    mother_qualification = models.CharField(
         max_length=100,
         null=True, 
         blank=True
    )
    mother_address = models.TextField(
         null=True, 
         blank=True
    )
    mother_phone_number = models.CharField(
         max_length=12, 
         null=True, 
         blank=True
    )
    mother_cell_number = models.CharField(
         max_length=12,
         null=True, 
         blank=True
    )
    emergency_number = models.CharField(
         max_length=15,
         null=True, 
         blank=True
    )
    
    def __str__(self):
            return f"{self.father_name}"

class Student(models.Model):
    CURRENT = 'current'
    LEFT = 'left'

    StudentStatus = [
        (CURRENT, 'Current'),
        (LEFT, 'Left')
    ]
    
    class Gender(models.TextChoices):
        MALE = 'M','Male'
        FEMALE = 'F','Female'
    
    class Class(models.TextChoices):
        BEGINNER = 'Be', 'Beginner'
        ELEMENTARY = 'El', 'Elementary'
        PREP = 'Pr', 'Prep'
        FIRST_GRADE = '1', 'One'
        SECOND_GRADE = '2', 'Two'
        THIRD_GRADE = '3', 'Three'
        FOURTH_GRADE = '4', 'Four'
        FIFTH_GRADE = '5', 'Five'
        SIXTH_GRADE = '6', 'Six'
        SEVENTH_GRADE = '7', 'Seven'
        EIGHTH_GRADE = '8', 'Eight'
        NINTH_GRADE = 'IX', 'Nine'
        TENTH_GRADE = 'X', 'Matric'
    
    class Section(models.TextChoices):
         A = 'A'
         B = 'B'
         C = 'C'
         D = 'D'
         E = 'E'
         F = 'F'   
    
    name = models.CharField(max_length=100)
    family = models.ForeignKey(
        FamilyInformation, 
        on_delete=models.PROTECT
    )
    gender = models.CharField(
        max_length=1, 
        choices=Gender.choices
    )
    date_of_birth = models.DateField()
    place_of_birth = models.TextField()
    religion = models.CharField(max_length=50)
    nationality = models.CharField(max_length=100)
    b_form_number = models.CharField(
        max_length=15,
        null=True, 
        blank=True
    )
    last_school = models.TextField(
        null=True, 
        blank=True
    )
    date_of_admission = models.DateField(auto_now_add=True)
    admitted_in_grade = models.CharField(
        max_length=2, 
        choices=Class.choices
    )
    status = models.CharField(
        max_length = 7, 
        choices = StudentStatus,
        default = CURRENT
    )
    academic_year = models.ForeignKey(
        Academic_Year,
        on_delete=models.CASCADE
    )
    section = models.CharField(
        max_length = 1, 
        choices = Section.choices,
        default = Section.A
    )
    roll_number = models.CharField(max_length=5)
    remarks = models.TextField(
        null=True, 
        blank=True
    )
    monthly_fees = models.IntegerField(
        validators=[MinValueValidator(0), 
                     MaxValueValidator(10000)]
    )
    admission_fees = models.IntegerField(
        validators=[MinValueValidator(0), 
                     MaxValueValidator(10000)]
    )
    examination_fees = models.IntegerField(
        validators=[MinValueValidator(0), 
                     MaxValueValidator(10000)]
    )
    board_fees = models.IntegerField(
        validators=[MinValueValidator(0), 
                     MaxValueValidator(10000)]
    )

    practical_fees = models.IntegerField(
        validators=[MinValueValidator(0), 
                     MaxValueValidator(10000)]
    )
    last_updated = models.DateField(auto_now=True)    
    
    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        if not self.monthly_fees:
            self.monthly_fees = self.academic_year.monthly_fees

        if not self.admission_fees:
            self.admission_fees = self.academic_year.admission_fees

        if not self.examination_fees:
            self.examination_fees = self.academic_year.examination_fees

        if not self.board_fees:
            self.board_fees = self.academic_year.board_fees

        if not self.practical_fees:
            self.practical_fees = self.academic_year.practical_fees

        super().save(*args, **kwargs)
