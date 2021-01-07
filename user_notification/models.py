from django.db import models
from datetime import datetime, timedelta
from django.conf import settings
from search_job.models import JobScope
from django.core.validators import MinValueValidator
from django.db.models import Q


class JobAlert(models.Model):
    user_account_id = models.ForeignKey(settings.AUTH_USER_MODEL,
                                        default=1,
                                        on_delete=models.CASCADE,
                                        blank=True,
                                        null=True)
    last_check_date = models.DateField(default=datetime.today)
    frequency_in_days = models.PositiveIntegerField(default=1,
                                                    validators=[MinValueValidator(1)])
    job_alert_type = models.CharField(max_length=50)
    job_alert_scope = models.CharField(max_length=50, choices=JobScope.choices, default=JobScope.UNSPECIFIED,
                                       blank=True, null=True)
    job_alert_city = models.CharField(max_length=50, blank=True, null=True)
    job_alert_company_name = models.CharField(
        max_length=20, blank=True, null=True)

    def __str__(self):
        return str(self.user_account_id)

    # Calculate the date of the next alert
    @classmethod
    def calc_check_date(cls, last_check_date, frequency_in_days):
        if frequency_in_days < 1:
            myError = ValueError(
                'frequency_in_days should be Greater than or equal to 1')
            raise myError
        else:
            if isinstance(last_check_date, datetime):
                res = last_check_date + timedelta(days=frequency_in_days)
            else:
                last_date = datetime.strptime(
                    last_check_date, "%Y-%m-%d").date()
                res = last_date + timedelta(days=frequency_in_days)
            return res

    @classmethod
    def check_if_alert_exist(cls, user_name):
        query = Q()
        query &= Q(user_account_id__username=user_name)
        alert_record = cls.objects.filter(query)
        if len(alert_record) > 0:
            return alert_record
        else:
            return "Job Alert Not Exist"


class JobType(models.Model):
    job_type_name = models.CharField(max_length=20)


class JobCity(models.Model):
    job_city_name = models.CharField(max_length=20)
