from django.db import models
from datetime import datetime, timedelta
from django.conf import settings
from searchJob.models import JobScope, JobPost
from django.core.validators import MinValueValidator
from django.core.mail import send_mail


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
            if isinstance(last_check_date, str):
                last_date = datetime.strptime(
                    last_check_date, "%Y-%m-%d").date()
                res = last_date + timedelta(days=frequency_in_days)
            else:
                res = last_check_date + timedelta(days=frequency_in_days)
            return res

    @classmethod
    def jobs_date_check(cls, jobs, last_check_date):
        if isinstance(last_check_date, str):
            last_check_date = datetime.strptime(
                last_check_date, "%Y-%m-%d").date()
        jobs = jobs.exclude(jobs.creation_date.date() <= last_check_date)
        return jobs

    @classmethod
    def CheckNewJobs(cls):
        alerts = cls.objects.all()
        for alert in alerts:
            last_check = alert.last_check_date
            days_delta = alert.frequency_in_days
            if JobAlert.calc_check_date(last_check, days_delta) == datetime.today().date():
                jobs = JobPost.GetSearchResults(
                    alert.job_alert_type, alert.job_alert_city,
                    alert.job_alert_scope, alert.job_alert_company_name)
                new_jobs = JobAlert.jobs_date_check(jobs, last_check)
                if new_jobs.count() > 0:
                    user = alert.user_account_id
                    user_mail = user.email
                    send_mail(
                        'job alert from joboard',
                        'Hi, there are new jobs that suits your requirements! you can check them out in the website',
                        settings.EMAIL_HOST_USER,
                        [user_mail],
                        fail_silently=False,
                    )
                alert.last_check_date = datetime.today()
                alert.save()


class JobType(models.Model):
    job_type_name = models.CharField(max_length=20)


class JobCity(models.Model):
    job_city_name = models.CharField(max_length=20)
