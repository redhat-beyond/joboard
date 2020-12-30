from django.shortcuts import render
from .models import JobPost


def jobs(request):
    if request.method == 'POST':
        JobType = request.POST.get('JobType')
        JobCity = request.POST.get('JobCity')
        JobScope = request.POST.get('JobScope')
        JobCompany = request.POST.get('JobCompany')

    job_posts = JobPost.GetSearchResults(JobType, JobCity, JobScope, JobCompany)
    return render(request, 'job_posts/job_post_list.html', {'job_posts': job_posts})
