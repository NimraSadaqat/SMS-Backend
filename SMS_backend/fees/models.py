from django.db import models, transaction
from django.core.validators import MinValueValidator, MaxValueValidator
from academic_year.models import Academic_Year
from students.models import Student

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
        return f"{self.id}-{self.student.name}:{self.dues_remaining}"

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

    def save(self, *args, **kwargs):
        # if not self.pk:  # If the object is being created (not updated)
            super().save(*args, **kwargs)
            amount_paid = self.amount_paid
            receipt = FeeReceipt.objects.last()
            print('receipt:', receipt)
            # receipt = FeeReceipt.objects.first()
            student_fees = StudentFeeReceipt.objects.all()  # Get PKs of related tags
            print('student_fees: ',student_fees)
            # for student_fee in student_fees:
            #     print(student_fee.dues_remaining)
            #     if amount_paid >= student_fee.dues_remaining:
            #         print('in loop1')
            #         print(amount_paid ,' >= ', student_fee.dues_remaining)
            #         amount_paid -= student_fee.dues_remaining
            #         print('amount paid remaining: ',amount_paid)
            #         StudentFee.objects.filter(pk = student_fee.pk).update(
            #             paid_amount = student_fee.dues_remaining,
            #             dues_remaining = 0,
            #             status = 'paid'
            #         )
            #     elif amount_paid < student_fee.dues_remaining:
            #         print('in loop2')
            #         print(amount_paid ,' < ', student_fee.dues_remaining)
            #         student_fee.dues_remaining = student_fee.dues_remaining - amount_paid
            #         print('amount paid remaining: ', amount_paid)
            #         print('student fee remaining: ',student_fee.dues_remaining)
            #         update_student_fee = StudentFee.objects.filter(id = student_fee.id)
            #         update_student_fee.update(
            #             paid_amount = amount_paid,
            #             dues_remaining = student_fee.dues_remaining
            #         )
            super().save(*args, **kwargs)
        
class StudentFeeReceipt(models.Model):
    receipt = models.ForeignKey(
        FeeReceipt, 
        on_delete = models.CASCADE
    )
    student_fee = models.ForeignKey(
        StudentFee,
        on_delete = models.CASCADE
    )

    @transaction.atomic
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.custom_function()

    def custom_function(self):
        # Your custom function logic here
        pass