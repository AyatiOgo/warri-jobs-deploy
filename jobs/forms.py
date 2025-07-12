from django import forms
from .models import JobsModel

class JobForm(forms.ModelForm):
    class Meta:
        model = JobsModel
        fields = ['title', 'description', 'company_name', 'job_type', 'work_location', 'categories',
                  'core_tasks', 'requirements', 'nice_to_have', 'benefits', 'contact_info', ]