import pytest
from django.contrib.auth.models import User
from user_notification.models import JobType, JobCity
from.models import JobPost, UserApplication, Company


@pytest.mark.parametrize('n,expected', [
    (("shakedch", "APPLIED"), "<QuerySet [<UserApplication: intel sw for students>, <UserApplication: intel QA>]>"),
    (("shakedch", None), "<QuerySet [<UserApplication: intel sw for students>, <UserApplication: intel QA>]>"),
    (("non_relevant", "APPLIED"), "No results found"),
    (("shakedch", "NOT_APPLIED"), "No results found"),
    (("itay11", "APPLIED"), "<QuerySet [<UserApplication: intel QA>, <UserApplication: Red Hat QA>]>"),
    (("itay11", "NOT_APPLIED"), "<QuerySet [<UserApplication: intel sw for students>]>"),
    (("itay11", None), "<QuerySet [<UserApplication: intel sw for students>, <UserApplication: intel QA>, "
                       "<UserApplication: Red Hat QA>]>"),
    ((None, "NOT_APPLIED"), "<QuerySet [<UserApplication: intel sw for students>]>"),
    ])
@pytest.mark.django_db
def testGetUserApplications(n, expected):

    # initialize the DB with data
    insertDataToDB()

    # Check few cases
    # Check assert (realFunctionResult, expected)
    assert str(UserApplication.GetUserApplications(*n)) == expected

    # Remove all the objects from DB
    deleteAllobjects()


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
    User.objects.filter(username="shakedch").delete()
    User.objects.filter(username="itay11").delete()
    UserApplication.objects.filter(application_status="NOT_APPLIED").delete()
    UserApplication.objects.filter(application_status="APPLIED").delete()


def insertDataToDB():
    job_type_new = JobType.objects.create(job_type_name="SW")

    job_city_new = JobCity.objects.create(job_city_name="tel aviv")

    company_new = Company.objects.create(company_name="intel",
                                         profile_description="American multinational corporation and technology "
                                                             "company",
                                         establishment_date="1968-07-18", contact_number="050-0000000",
                                         company_type="SW",
                                         company_url="https://www.intel.co.il/content/www/il/he/homepage.html")

    job_post_new = JobPost.objects.create(job_type_id=job_type_new, company_id=company_new, job_city_id=job_city_new,
                                          job_name="intel sw for students",
                                          job_description="the best job",
                                          job_scope="STUDENT", job_URL="intelstujobs.com")

    job_type_new2 = JobType.objects.create(job_type_name="QA")

    job_post_new2 = JobPost.objects.create(job_type_id=job_type_new2,
                                           company_id=company_new, job_city_id=job_city_new, job_name="intel QA",
                                           job_description="good job", job_scope="PART", job_URL="intelparjobs.com")

    company_new2 = Company.objects.create(company_name="Red Hat",
                                          profile_description="The world's leading provider "
                                                              "of enterprise open source solutions",
                                          establishment_date="1993-03-26", contact_number="09-769-2222",
                                          company_type="SW", company_url="https://www.redhat.com/en")

    job_city_new2 = JobCity.objects.create(job_city_name="raanana")

    job_post_new3 = JobPost.objects.create(job_type_id=job_type_new2,
                                           company_id=company_new2, job_city_id=job_city_new2, job_name="Red Hat QA",
                                           job_description="wow", job_scope="STUDENT",
                                           job_URL="https://www.redhat.com/en/jobs")

    user_new = User.objects.create_user(username="shakedch", password="1234", email="shaked@example.com")

    UserApplication.objects.create(user_account_id=user_new, job_post_id=job_post_new,
                                   application_status="APPLIED")

    UserApplication.objects.create(user_account_id=user_new, job_post_id=job_post_new2,
                                   application_status="APPLIED")

    user_new2 = User.objects.create_user(username="itay11", password="1111", email="itay@example.com")

    UserApplication.objects.create(user_account_id=user_new2, job_post_id=job_post_new,
                                   application_status="NOT_APPLIED")

    UserApplication.objects.create(user_account_id=user_new2, job_post_id=job_post_new2,
                                   application_status="APPLIED")

    UserApplication.objects.create(user_account_id=user_new2, job_post_id=job_post_new3,
                                   application_status="APPLIED")
