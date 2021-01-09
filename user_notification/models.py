from django.db import models
from datetime import datetime, timedelta
from django.conf import settings
from search_job.models import JobScope, JobPost
from django.core.validators import MinValueValidator
from django.db.models import Q
from django.core.mail import send_mail
from django.db.models.query import QuerySet


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

    @classmethod
    def calc_next_alert_date(cls, last_check_date, frequency_in_days):
        # Calculate the date of the next alert
        if frequency_in_days < 1:
            raise ValueError(
                'frequency_in_days should be Greater than or equal to 1')
        else:
            res = last_check_date + timedelta(days=frequency_in_days)
            return res

    @classmethod
    def check_if_alert_exist(cls, user_name):
        query = Q()
        query &= Q(user_account_id__username=user_name)
        alert_record = cls.objects.filter(query)
        if len(alert_record) < 1:
            return "Job Alert Not Exist"
        return alert_record

    @classmethod
    def exclude_old_jobs(cls, jobs, last_check_date):
        # Excludes old job posts by comparing their creation date with last check date
        if isinstance(jobs, QuerySet):
            for job in jobs:
                if job.creation_date.date() <= last_check_date:
                    jobs = jobs.exclude(id=job.id)
            return jobs
        return JobPost.objects.none()

    @classmethod
    def send_mail(cls, jobs, alert):
        # Sends mail to the user to inform there are new relevant job posts after checking there are such job posts
        if jobs.count() <= 0:
            return
        user = alert.user_account_id
        user_mail = user.email
        send_mail(
            'job alert from joboard',
            'Hi, there are new jobs that suits your requirements! you can check them out in the website',
            settings.EMAIL_HOST_USER,
            [user_mail],
            fail_silently=False,
        )

    @classmethod
    def send_alert_for_new_jobs(cls):
        '''The main function of the alerts - checks if the date of sending the alert to the user has arrived
        and if there are indeed new job posts that comply with the requirements and should be alerted'''
        alerts = cls.objects.all()
        for alert in alerts:
            last_check = alert.last_check_date
            days_delta = alert.frequency_in_days
            if JobAlert.calc_check_date(last_check, days_delta) == datetime.today().date():
                jobs = JobPost.GetSearchResults(
                    alert.job_alert_type, alert.job_alert_city,
                    alert.job_alert_scope, alert.job_alert_company_name)
                new_jobs = JobAlert.jobs_date_check(jobs, last_check)
                JobAlert.send_mail(new_jobs, alert)
                alert.last_check_date = datetime.today()
                alert.save()


class JobType(models.Model):
    job_type_name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.job_type_name)


class JobCity(models.Model):
    job_city_name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.job_city_name)
