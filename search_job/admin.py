from django.contrib import admin
from .models import Company, JobPost, UserApplication


admin.site.register(Company)
admin.site.register(JobPost)
admin.site.register(UserApplication)
