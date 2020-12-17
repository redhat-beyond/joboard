from django.db import models


class CompanyType(models.TextChoices):
    FINTECH = 'FINTECH', 'FINTECH'
    BIOTECH = 'BIOTECH', 'BIOTECH'
    MEDTECH = 'MEDTECH', 'MEDTECH'
    FOODTECH = 'FOODTECH', 'FOODTECH'
    AUTOMATIVE = 'AUTOMATIVE', 'AUTOMATIVE'
    SW = 'SW', 'SW'
    HW = 'HW', 'HW'
    UNSPECIFIED = 'UNSPECIFIED', 'UNSPECIFIED'


class JobScope(models.TextChoices):
    FULL = 'FULL', 'FULL'
    PART = 'PART', 'PART'
    INTER = 'INTER', 'INTER'
    STUDENT = 'STUDENT', 'STUDENT'
    UNSPECIFIED = 'UNSPECIFIED', 'UNSPECIFIED'


class ApplicationStatus(models.TextChoices):
    APPLIED = 'APPLIED', 'APPLIED'
    NOT_APPLIED = 'NOT_APPLIED', 'NOT_APPLIED'
    UNSPECIFIED = 'UNSPECIFIED', 'UNSPECIFIED'


class Company(models.Model):
    company_name = models.CharField(max_length=100)
    profile_description = models.TextField()
    establishment_date = models.DateField()
    contact_number = models.CharField(max_length=12, blank=True, null=True)
    company_type = models.CharField(max_length=50, choices=CompanyType.choices, default=CompanyType.UNSPECIFIED,
                                    blank=True, null=True)
    company_url = models.URLField(max_length=200)

    def __str__(self):
        return self.company_name


class JobPost(models.Model):
    job_type_id = models.ForeignKey("user_notification.JobType", on_delete=models.CASCADE, blank=True, null=True)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    job_city_id = models.ForeignKey("user_notification.JobCity", on_delete=models.CASCADE, blank=True, null=True)
    job_name = models.CharField(max_length=100)
    job_description = models.TextField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add=True)
    job_scope = models.CharField(max_length=50, choices=JobScope.choices, default=JobScope.UNSPECIFIED,
                                 blank=True, null=True)
    job_URL = models.URLField(max_length=200)

    def __str__(self):
        return self.job_name


class UserApplication(models.Model):
    user_account_id = models.ForeignKey("login.UserAccount", on_delete=models.CASCADE, blank=True, null=True)
    job_post_id = models.ForeignKey(JobPost, on_delete=models.CASCADE, blank=True, null=True)
    application_status = models.CharField(max_length=50, choices=ApplicationStatus.choices,
                                          default=ApplicationStatus.UNSPECIFIED, blank=True, null=True)

    def __str__(self):
        return str(self.job_post_id)
