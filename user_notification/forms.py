from django import forms
from . import models


class CreateJobAlert(forms.ModelForm):
    class Meta:
        model = models.JobAlert
        fields = ['user_account_id', 'alert_frequency', 'job_alert_type',
                  'job_alert_scope', 'job_alert_city', 'job_alert_company_name']
