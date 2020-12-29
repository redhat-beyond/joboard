from user_notification.models import JobAlert
import pytest
from datetime import datetime


# test for calc_check_day
@pytest.mark.parametrize('n, x, expected', [
    ("2020-12-27", 2, "2020-12-29"),
    ("2020-12-27", 3, "2020-12-30"),
    (datetime.strptime("2020-12-27", "%Y-%m-%d").date(), 10, "2021-01-06"),
])
def test_calc_check_date(n, x, expected):
    assert JobAlert.calc_check_date(
        n, x) == datetime.strptime(expected, "%Y-%m-%d").date()


@pytest.mark.parametrize('n, x', [
    ("2020-12-27", -2),
    ("2020-12-27", 0),
    ("2020-12-27", -5),
])
def test_exception(n, x):
    with pytest.raises(Exception) as excinfo:
        JobAlert.calc_check_date(n, x)
    assert str(
        excinfo.value) == 'frequency_in_days should be Greater than or equal to 1'
