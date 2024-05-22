from django.db.models.signals import post_save
from django.dispatch import receiver
from fees.models import Fees, StudentFee
from students.models import Student


@receiver(post_save, sender=Fees)
def generate_student_fees(sender, instance, created, **kwargs):
    if created:
        try:
            students = Student.objects.filter(academic_year=instance.academic_year)
        except:
            students = None
        if students is not None:
            for student in students:
                student_amount = Student.objects.get(pk = student.pk)
                if instance.type == 'Mon':
                    StudentFee.objects.create(
                        student = student, 
                        fee = instance, 
                        dues_remaining = student_amount.monthly_fees
                    )
                elif instance.type == 'Exm':
                    StudentFee.objects.create(
                        student = student, 
                        fee = instance, 
                        dues_remaining = student_amount.examination_fees
                    )
                elif instance.type == 'Adm':
                    StudentFee.objects.create(
                        student = student, 
                        fee = instance, 
                        dues_remaining = student_amount.admission_fees
                    )
                elif instance.type == 'Brd':
                    StudentFee.objects.create(
                        student = student, 
                        fee = instance, 
                        dues_remaining = student_amount.board_fees
                    )
                elif instance.type == 'Prc':
                    StudentFee.objects.create(
                        student = student, 
                        fee = instance, 
                        dues_remaining = student_amount.practical_fees
                    )
                elif instance.type == 'Oth':
                    StudentFee.objects.create(
                        student = student, 
                        fee = instance, 
                        dues_remaining = instance.other_charges
                    )