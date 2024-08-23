from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction
from fees.models import Fees, StudentFee, FeeReceipt, StudentFeeReceipt
from students.models import Student
from finance.models import Default, MonthlyIncome
from django.utils import timezone


@receiver(post_save, sender=Fees)
def generate_student_fees(sender, instance, created, **kwargs):
    if created:
        try:
            students = Student.objects.filter(academic_year=instance.academic_year)
            print('students:', students)
        except:
            students = None
        if students is not None:
            total_fee_amount = 0
            for student in students:
                student_amount = Student.objects.get(pk = student.pk)
                if instance.type == 'Mon':
                    StudentFee.objects.create(
                        student = student, 
                        fee = instance, 
                        dues_remaining = student_amount.monthly_fees
                    )
                    total_fee_amount += student_amount.monthly_fees
                elif instance.type == 'Exm':
                    StudentFee.objects.create(
                        student = student, 
                        fee = instance, 
                        dues_remaining = student_amount.examination_fees
                    )
                    total_fee_amount += student_amount.examination_fees
                elif instance.type == 'Adm':
                    StudentFee.objects.create(
                        student = student, 
                        fee = instance, 
                        dues_remaining = student_amount.admission_fees
                    )
                    total_fee_amount += student_amount.admission_fees
                elif instance.type == 'Brd':
                    StudentFee.objects.create(
                        student = student, 
                        fee = instance, 
                        dues_remaining = student_amount.board_fees
                    )
                    total_fee_amount += student_amount.board_fees
                elif instance.type == 'Prc':
                    StudentFee.objects.create(
                        student = student, 
                        fee = instance, 
                        dues_remaining = student_amount.practical_fees
                    )
                    total_fee_amount += student_amount.practical_fees
                elif instance.type == 'Oth':
                    StudentFee.objects.create(
                        student = student, 
                        fee = instance, 
                        dues_remaining = instance.other_charges
                    )
                    total_fee_amount += student_amount.other_charges
                
            # Update the Default model with the total fee amount
            current_time = timezone.now()
            month = current_time.month
            year = current_time.year
            
            # Update or create the Default model instance for the current month and year
            default_obj, created = Default.objects.get_or_create(
                created_at__year=year,
                created_at__month=month,
                defaults={'amount': 0}
            )
            default_obj.amount += total_fee_amount
            default_obj.save()

@receiver(post_save, sender=FeeReceipt)
def apply_fees_logic(sender, instance, created, **kwargs):
    if getattr(instance, '_processed', False):
        return  # Skip if the instance has already been processed

    # Use transaction.on_commit to defer processing until after the commit
    transaction.on_commit(lambda: process_fees_logic(instance))

@transaction.atomic
def process_fees_logic(instance):
    amount_paid = instance.amount_paid + instance.discount
    student_fees = StudentFeeReceipt.objects.filter(receipt=instance)
    print('student_fees:', student_fees)
    for student_fee_receipt in student_fees:
        student_fee = student_fee_receipt.student_fee

        if amount_paid >= student_fee.dues_remaining:
            amount_paid -= student_fee.dues_remaining
            student_fee.paid_amount += student_fee.dues_remaining
            student_fee.dues_remaining = 0
            student_fee.status = 'paid'
        else:
            student_fee.paid_amount += amount_paid
            student_fee.dues_remaining -= amount_paid
            amount_paid = 0

        student_fee.save()

    # Update Default model
    default_obj, _ = Default.objects.get_or_create()
    default_obj.amount -= instance.amount_paid + instance.discount
    default_obj.save()

    # Update MonthlyIncome model
    monthly_income, _ = MonthlyIncome.objects.get_or_create()
    monthly_income.amount += instance.amount_paid
    monthly_income.discount += instance.discount
    monthly_income.save()

    # Mark as generated and save the instance
    instance.generated = True
    instance._processed = True  # Set the flag to avoid recursion
    instance.save(update_fields=['generated'])