from django.shortcuts import render
from.models import JobPost


def jobs(request):
    job_posts = JobPost.objects.all().order_by('creation_date')
    return render(request, 'job_posts/job_post_list.html', {'job_posts': job_posts})
