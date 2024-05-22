from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Academic_Year(models.Model):
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

    start_date =  models.DateField()
    end_date = models.DateField()
    grade = models.CharField(
         max_length=2, 
         choices=Class.choices
        )
    monthly_fees = models.IntegerField(
        validators=[MinValueValidator(100), 
                     MaxValueValidator(10000)]
    )
    admission_fees = models.IntegerField(
        validators=[MinValueValidator(100), 
                     MaxValueValidator(10000)]
    )
    examination_fees = models.IntegerField(
        validators=[MinValueValidator(100), 
                     MaxValueValidator(10000)]
    )
    board_fees = models.IntegerField(
        validators=[MinValueValidator(100), 
                     MaxValueValidator(10000)],
        blank = True,
        null = True
    )
    practical_fees = models.IntegerField(
        validators=[MinValueValidator(100), 
                     MaxValueValidator(10000)],
        blank = True,
        null = True
    )

    def __str__(self):
        return f"{self.start_date.year}-{self.end_date.year}: {self.grade}"
