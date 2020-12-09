from django.contrib import admin
from .models import JobAlert, JobType, JobCity

# Register your models here.
admin.site.register(JobAlert)
admin.site.register(JobType)
admin.site.register(JobCity)
