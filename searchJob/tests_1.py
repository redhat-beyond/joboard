from user_notification.models import JobType, JobCity
import pytest
from.models import Company, JobPost


@pytest.mark.parametrize('n,expected', [
    (("non_relevant", "non_relevant", "non_relevant", "non_relevant"), "no relevant jobs for you"),
    (("SW", None, None, None), ['intel sw for students']),
    (("SW", "tel aviv", "STUDENT", "intel"), ['intel sw for students']),
    (("SW", "tel aviv", None, None), ['intel sw for students']),
    ((None, "tel aviv", None, None), ['intel sw for students', 'intel QA']),
    (("QA", "tel aviv", None, "intel"), ['intel QA']),
    ((None, None, None, "intel"), ['intel sw for students', 'intel QA']),
    (("QA", None, None, None), ['intel QA', 'Red Hat QA']),
    ((None, None, "STUDENT", None), ['intel sw for students', 'Red Hat QA']),
    (("QA", "raanana", None, None),  ['Red Hat QA']),
    ((None, "raanana", None, None), ['Red Hat QA']),
    ((None, None, "PART", None), ['intel QA']),
    ((None, "raanana", "PART", None), "no relevant jobs for you"),
    ((None, "raanana", None, "intel"), "no relevant jobs for you"),
    (("DevOps", None, None, None), "no relevant jobs for you"),
    ((None, None, "FULL", None), "no relevant jobs for you"),
    ])
@pytest.mark.django_db
def testGetSearchResults1(n, expected):

    # initialize the DB with data
    insertDataToDB()

    # Check few cases
    # Check assert (realFunctionResult, expected)
    assert JobPost.GetSearchResults(*n) == expected

    # Remove all the objects from DB
    deleteAllobjects()


@pytest.mark.django_db
def testGetSearchResults2():
    # Free search when the courent DB is empty
    unfiltered_search = (None, None, None, None)
    checkIfDBContainsObjects(unfiltered_search)


@pytest.mark.django_db
def testGetSearchResults3():
    # initialize the DB with data
    insertDataToDB()

    # Free search when the DB is not empty
    unfiltered_search = (None, None, None, None)
    assert JobPost.GetSearchResults(*unfiltered_search) == \
           list(JobPost.objects.all().values_list('job_name', flat=True).all())


@pytest.mark.django_db
def testGetSearchResults4():
    # Remove all the objects from DB
    deleteAllobjects()

    # Check that all the new objects are removed
    unfiltered_search = (None, None, None, None)
    checkIfDBContainsObjects(unfiltered_search)


def checkIfDBContainsObjects(unfiltered_search):
    assert JobPost.GetSearchResults(*unfiltered_search) == "no relevant jobs for you"


def deleteAllobjects():
    JobPost.objects.filter(job_name="intel sw for students").delete()
    JobType.objects.filter(job_type_name="SW").delete()
    JobCity.objects.filter(job_city_name="tel aviv").delete()
    Company.objects.filter(company_name="intel").delete()
    JobType.objects.filter(job_type_name="QA").delete()
    JobPost.objects.filter(job_name="intel QA").delete()
    Company.objects.filter(company_name="Red Hat").delete()
    JobCity.objects.filter(job_city_name="raanana").delete()
    JobPost.objects.filter(job_name="Red Hat QA").delete()


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
