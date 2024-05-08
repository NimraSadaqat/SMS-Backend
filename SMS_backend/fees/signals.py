from django.db.models.signals import post_save
from django.dispatch import receiver
from fees.models import Fees, StudentFee, Academic_Year
from students.models import Student


@receiver(post_save, sender=Fees)
def generate_student_fees(sender, instance, created, **kwargs):
    if created:
        students = Student.objects.filter(academic_year=instance.academic_year)
        for student in students:
            StudentFee.objects.create(student=student, fee=instance)