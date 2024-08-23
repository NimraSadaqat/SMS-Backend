from django.db import models, transaction
from django.core.validators import MinValueValidator, MaxValueValidator
from academic_year.models import Academic_Year
from students.models import Student
from finance.models import Default, MonthlyIncome

# Create your models here.
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
    other_charges = models.PositiveIntegerField(
        validators=[MinValueValidator(0), 
                     MaxValueValidator(100000)],
        default = 0
    )
    description = models.CharField(max_length=100)
    amount = models.PositiveIntegerField(
        validators=[MinValueValidator(0), 
                     MaxValueValidator(100000)],
        default = 0
    )
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.academic_year}---{self.type}---{self.created_at}"
    
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
            else:
                self.amount = 0
        super().save(*args, **kwargs)

class StudentFee(models.Model):
    class Status(models.TextChoices):
        PAID = 'paid', 'Paid'
        UNPAID = 'unpaid', 'Unpaid'

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    fee = models.ForeignKey(
        Fees, 
        on_delete=models.CASCADE
    )
    status = models.CharField(
        max_length = 6,
        choices = Status.choices,
        default = 'unpaid'
    )
    dues_remaining = models.PositiveIntegerField(
        validators=[MinValueValidator(0), 
                     MaxValueValidator(100000)],
        default = 0
    )
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    paid_amount = models.PositiveIntegerField(
        validators=[MinValueValidator(0), 
                     MaxValueValidator(100000)],
        default = 0
    )

    def __str__(self):
        return f"{self.student.academic_year}-{self.student.name}:{self.dues_remaining}"

class FeeReceipt(models.Model):
    student_fees = models.ManyToManyField(StudentFee, through='StudentFeeReceipt')
    fees_received_by = models.CharField(max_length=100)
    manual_fee_receipt_number = models.CharField(max_length = 5)
    fees_paid_on = models.DateTimeField(auto_now_add = True)
    discount = models.PositiveIntegerField(
        validators=[MinValueValidator(0), 
                     MaxValueValidator(100000)],
        default = 0
    )
    amount_paid = models.PositiveIntegerField(
        validators=[MinValueValidator(0), 
                     MaxValueValidator(100000)],
        default = 0
    )
    generated = models.BooleanField(default = False)

class StudentFeeReceipt(models.Model):
    receipt = models.ForeignKey(
        FeeReceipt, 
        on_delete = models.CASCADE
    )
    student_fee = models.ForeignKey(
        StudentFee,
        on_delete = models.CASCADE
    )