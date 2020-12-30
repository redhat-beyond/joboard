from django.db.models import Q
from django.db import models
from django.conf import settings


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
    INTERN = 'INTERN', 'INTERN'
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
    company_type = models.CharField(max_length=50,
                                    choices=CompanyType.choices,
                                    default=CompanyType.UNSPECIFIED,
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

    # filter DB objects (job posts) based on optional search fields
    @classmethod
    def GetSearchResults(cls, JobType=None, JobCity=None, JobScope=None, Company=None):
        query = Q()
        if JobType:
            query &= Q(job_type_id__job_type_name=JobType)
        if JobCity:
            query &= Q(job_city_id__job_city_name=JobCity)
        if JobScope:
            query &= Q(job_scope=JobScope)
        if Company:
            query &= Q(company_id__company_name=Company)

        filter_query = cls.objects.filter(query).order_by('creation_date')
        if len(filter_query) < 1:
            return "no relevant jobs for you"
        return list(filter_query.values_list('job_name', flat=True).all())


class UserApplication(models.Model):
    user_account_id = models.ForeignKey(settings.AUTH_USER_MODEL, default=1,
                                        on_delete=models.CASCADE, blank=True, null=True)
    job_post_id = models.ForeignKey(JobPost, on_delete=models.CASCADE, blank=True, null=True)
    application_status = models.CharField(max_length=50, choices=ApplicationStatus.choices,
                                          default=ApplicationStatus.UNSPECIFIED, blank=True, null=True)

    def __str__(self):
        return str(self.job_post_id)

    # filter DB objects (User application) based on user
    @classmethod
    def GetUserApplications(cls, UserName=None, ApplicationStatus=None):
        query = Q()
        if UserName:
            query &= Q(user_account_id__username=UserName)
        if ApplicationStatus:
            query &= Q(application_status=ApplicationStatus)
        filter_query = cls.objects.filter(query)
        if len(filter_query) < 1:
            return "No results found"
        return filter_query
