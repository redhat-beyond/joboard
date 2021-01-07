from user_notification.models import JobAlert
import pytest
from datetime import datetime
from django.contrib.auth.models import User


@pytest.mark.parametrize('n, x, expected', [
    ("2020-12-27", 2, "2020-12-29"),
    ("2020-12-27", 3, "2020-12-30"),
    ("2020-12-27", 10, "2021-01-06"),
])
def test_calc_next_alert_date(n, x, expected):
    # datetime.strptime converts string to datetime
    n = datetime.strptime(n, "%Y-%m-%d").date()
    assert JobAlert.calc_next_alert_date(
        n, x) == datetime.strptime(expected, "%Y-%m-%d").date()


@pytest.mark.parametrize('n, x', [
    ("2020-12-27", -2),
    ("2020-12-27", 0),
    ("2020-12-27", -5),
])
def test_exception(n, x):
    with pytest.raises(Exception) as excinfo:
        JobAlert.calc_next_alert_date(n, x)
    assert str(
        excinfo.value) == 'frequency_in_days should be Greater than or equal to 1'


# Tests to check if alest details are correct

@pytest.mark.parametrize('n,expected', [
    ("Yosi", "<QuerySet [<JobAlert: Yosi>]>"),
    ("Tami", "<QuerySet [<JobAlert: Tami>]>"),
    ("Itay", "Job Alert Not Exist"),
])
@pytest.mark.django_db
def test_check_if_alert_exist(n, expected):
    insertDataToDB()
    assert str(JobAlert.check_if_alert_exist(n)) == expected


def deleteAllobjects():
    JobAlert.objects.new_user1.delete()
    JobAlert.objects.new_user2.delete()
    User.objects.filter(username="Yosi").delete()
    User.objects.filter(username="Tami").delete()


def insertDataToDB():
    new_user1 = User.objects.create_user(
        username="Yosi", password="1111", email="yosi@example.com")
    JobAlert.objects.create(user_account_id=new_user1,
                            frequency_in_days=5, job_alert_type="Student", job_alert_scope="Full",
                            job_alert_city="Tel Aviv", job_alert_company_name="Google")
    new_user2 = User.objects.create_user(
        username="Tami", password="2222", email="tami@example.com")
    JobAlert.objects.create(user_account_id=new_user2,
                            frequency_in_days=7, job_alert_type="Junior", job_alert_scope="Full",
                            job_alert_city="Haifa", job_alert_company_name="")
