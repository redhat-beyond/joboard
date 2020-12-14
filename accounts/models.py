from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Gender(models.TextChoices):
    MALE = 'M', 'Male'
    FEMALE = 'F', 'Female'
    NONBINARY = 'NB', 'Nonbinary'
    UNSPECIFIED = 'U', 'Unspecified'


class UserAccount(models.Model):
    user = models.OneToOneField(User, related_name='useraccount', on_delete=models.CASCADE, null=True)
    gender = models.CharField(max_length=2, choices=Gender.choices, default=Gender.UNSPECIFIED)
    contact_number = models.CharField(max_length=12, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    # future addition: email verification
    # email_validated = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_account(sender, instance, created, **kwargs):
    if created:
        UserAccount.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_account(sender, instance, **kwargs):
    instance.useraccount.save()
