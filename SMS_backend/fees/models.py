from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from academic_year.models import Academic_Year
from students.models import Student

# Create your models here.
class Expenses(models.Model):
    description = models.CharField(max_length=100)
    amount = models.IntegerField(
        validators=[MinValueValidator(0), 
                     MaxValueValidator(10000)]
    )
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Fees(models.Model):
    
    class FeesType(models.TextChoices):
        MONTHLY = 'Mon', 'Monthly'
        ADMISSION = 'Adm', 'Admission'
        EXAMINATION = 'Exm', 'Examination'
        BOARD = 'Brd', 'Board'
        PRACTICAL = 'Prc', 'Practical'
        OTHER = 'Oth', 'Other'
    
    academic_year = models.ForeignKey(
        Academic_Year,
        on_delete = models.CASCADE
    )
    type = models.CharField(
        max_length = 3,
        choices = FeesType.choices
    )
    other_charges = models.IntegerField(
        validators=[MinValueValidator(0), 
                     MaxValueValidator(100000)],
        null = True,
        blank = True
    )
    description = models.CharField(max_length=100)
    amount = models.IntegerField(
        validators=[MinValueValidator(0), 
                     MaxValueValidator(100000)]
    )
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.amount:  # Only set if amount is empty
            if self.type == 'Mon':
                self.amount = self.academic_year.monthly_fees
            elif self.type == 'Adm':
                self.amount = self.academic_year.admission_fees
            elif self.type == 'Exm':
                self.amount = self.academic_year.examination_fees
            elif self.type == 'Brd':
                self.amount = self.academic_year.board_fees
            elif self.type == 'Prc':
                self.amount = self.academic_year.practical_fees
            elif self.type == 'Oth':
                self.amount = self.other_charges
        super().save(*args, **kwargs)
    
class StudentFee(models.Model):
    class Status(models.TextChoices):
        PAID = 'paid', 'Paid'
        UNPAID = 'unpaid', 'Unpaid'

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    fee = models.ForeignKey(Fees, on_delete=models.CASCADE)
    status = models.CharField(
        max_length = 6,
        choices = Status.choices,
        default = 'unpaid'
    )
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    paid_amount = models.IntegerField(
        validators=[MinValueValidator(0), 
                     MaxValueValidator(100000)],
        default = 0
    )

