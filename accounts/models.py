from django.db import models
from django.contrib.auth.models import User


class Gender(models.TextChoices):
    MALE = 'M', 'Male'
    FEMALE = 'F', 'Female'
    NONBINARY = 'NB', 'Nonbinary'
    UNSPECIFIED = 'U', 'Unspecified'


class UserAccount(models.Model):
    user = models.OneToOneField(User, related_name='useraccount', on_delete=models.CASCADE, blank=True, null=True)
    gender = models.CharField(max_length=2, choices=Gender.choices, default=Gender.UNSPECIFIED)
    contact_number = models.CharField(max_length=12, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    # future addition: email verification
    # email_validated = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
