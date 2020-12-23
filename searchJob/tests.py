from user_notification.models import JobType, JobCity
import pytest
from.models import Company, JobPost


@pytest.mark.parametrize('n,expected', [
    (("non_relevant", "non_relevant", "non_relevant", "non_relevant"), "no relevant jobs for you"),
    (("SW", None, None, None), "<QuerySet [<JobPost: intel sw for students>]>"),
    (("SW", "tel aviv", "STUDENT", "intel"), "<QuerySet [<JobPost: intel sw for students>]>"),
    (("SW", "tel aviv", None, None), "<QuerySet [<JobPost: intel sw for students>]>"),
    ((None, "tel aviv", None, None), "<QuerySet [<JobPost: intel sw for students>, <JobPost: intel QA>]>"),
    (("QA", "tel aviv", None, "intel"), "<QuerySet [<JobPost: intel QA>]>"),
    ((None, None, None, "intel"), "<QuerySet [<JobPost: intel sw for students>, <JobPost: intel QA>]>"),
    (("QA", None, None, None), "<QuerySet [<JobPost: intel QA>, <JobPost: Red Hat QA>]>"),
    ((None, None, "STUDENT", None), "<QuerySet [<JobPost: intel sw for students>, <JobPost: Red Hat QA>]>"),
    (("QA", "raanana", None, None), "<QuerySet [<JobPost: Red Hat QA>]>"),
    ((None, "raanana", None, None), "<QuerySet [<JobPost: Red Hat QA>]>"),
    ((None, None, "PART", None), "<QuerySet [<JobPost: intel QA>]>"),
    ((None, "raanana", "PART", None), "no relevant jobs for you"),
    ((None, "raanana", None, "intel"), "no relevant jobs for you"),
    (("DevOps", None, None, None), "no relevant jobs for you"),
    ((None, None, "FULL", None), "no relevant jobs for you"),
    ])
@pytest.mark.django_db
def testGetSearchResults(n, expected):
    unfiltered_search = (None, None, None, None)

    # Free search when the courent DB is empty
    checkIfDBContainsObjects(unfiltered_search)

    # initialize the DB with data
    insertDataToDB()

    # Free search when the DB is not empty
    assert str(JobPost.GetSearchResults(*unfiltered_search)) == str(JobPost.objects.all())

    # Check few cases
    # Check assert (realFunctionResult, expected)
    assert str(JobPost.GetSearchResults(*n)) == expected

    # Remove all the objects from DB
    deleteAllobjects()

    # Check that all the new objects are removed
    checkIfDBContainsObjects(unfiltered_search)


def checkIfDBContainsObjects(unfiltered_search):
    assert str(JobPost.GetSearchResults(*unfiltered_search)) == "no relevant jobs for you"


def deleteAllobjects():
    JobPost.objects.all().delete()
    JobType.objects.all().delete()
    JobCity.objects.all().delete()
    Company.objects.all().delete()


def insertDataToDB():
    job_type_new = JobType.objects.create(job_type_name="SW")

    job_city_new = JobCity.objects.create(job_city_name="tel aviv")

    company_new = Company.objects.create(company_name="intel",
                                         profile_description="American multinational corporation and technology "
                                                             "company",
                                         establishment_date="1968-07-18", contact_number="050-0000000",
                                         company_type="SW",
                                         company_url="https://www.intel.co.il/content/www/il/he/homepage.html")

    JobPost.objects.create(job_type_id=job_type_new, company_id=company_new, job_city_id=job_city_new,
                           job_name="intel sw for students",
                           job_description="the best job",
                           job_scope="STUDENT", job_URL="intelstujobs.com")

    job_type_new2 = JobType.objects.create(job_type_name="QA")

    JobPost.objects.create(job_type_id=job_type_new2,
                           company_id=company_new, job_city_id=job_city_new, job_name="intel QA",
                           job_description="good job", job_scope="PART", job_URL="intelparjobs.com")

    company_new2 = Company.objects.create(company_name="Red Hat",
                                          profile_description="The world's leading provider "
                                                              "of enterprise open source solutions",
                                          establishment_date="1993-03-26", contact_number="09-769-2222",
                                          company_type="SW", company_url="https://www.redhat.com/en")

    job_city_new2 = JobCity.objects.create(job_city_name="raanana")

    JobPost.objects.create(job_type_id=job_type_new2,
                           company_id=company_new2, job_city_id=job_city_new2, job_name="Red Hat QA",
                           job_description="wow", job_scope="STUDENT",
                           job_URL="https://www.redhat.com/en/jobs")
