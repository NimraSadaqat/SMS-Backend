from django.db.models.signals import post_save
from django.dispatch import receiver
from fees.models import Fees,StudentFee
from students.models import Student


@receiver(post_save, sender = Student)
def generate_student_admission_fees(sender, instance, created, **kwargs):
    if created:
        try:
            feeses = Fees.objects.filter(
                academic_year = instance.academic_year, 
            )
        except:
            feeses = None
        if feeses is not None:
            for fees in feeses:
                if fees.type == 'Adm':
                    StudentFee.objects.create(
                        student = instance,
                        fee = fees,
                        amount = instance.admission_fees
                    )
                if fees.type == 'Exm':
                    StudentFee.objects.create(
                        student = instance,
                        fee = fees,
                        amount = instance.examination_fees
                    )
                if fees.type == 'Prc':
                    StudentFee.objects.create(
                        student = instance,
                        fee = fees,
                        amount = instance.practical_fees
                    )
                if fees.type == 'Brd':
                    StudentFee.objects.create(
                        student = instance,
                        fee = fees,
                        amount = instance.board_fees
                    )
