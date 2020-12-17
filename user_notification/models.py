from django.db import models

# Create your models here.


class JobAlert(models.Model):
    user_account_id = models.ForeignKey(
        "accounts.UserAccount", on_delete=models.CASCADE, blank=True, null=True)
    alert_message = models.TextField()
    alert_frequency = models.CharField(max_length=20)
    job_alert_type = models.CharField(max_length=50)
    job_alert_scope = models.CharField(max_length=50)
    job_alert_city = models.CharField(max_length=50)
    job_alert_company_name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.user_account_id)


class JobType(models.Model):
    job_type_name = models.CharField(max_length=20)


class JobCity(models.Model):
    job_city_name = models.CharField(max_length=20)
