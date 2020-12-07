from django.db import models


class Gender(models.TextChoices):
    MALE = 'M', 'Male'
    FEMALE = 'F', 'Female'
    NONBINARY = 'NB', 'Nonbinary'
    UNSPECIFIED = 'U', 'Unspecified'


class UserAccount(models.Model):
    user_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    gender = models.CharField(max_length=2, choices=Gender.choices, default=Gender.UNSPECIFIED, blank=True, null=True)
    contact_number = models.CharField(max_length=12, blank=True, null=True)
    user_birth_date = models.DateField()
    user_email = models.EmailField(max_length=254, null=True)
