from user_notification.models import JobAlert
import pytest
from datetime import datetime


# test for calc_check_day
@pytest.mark.parametrize('n, x, expected', [
    ("2020-12-27", 2, "2020-12-29"),
    ("2020-12-27", 3, "2020-12-30"),
    ("2020-12-27", 10, "2021-01-06"),
])
def test_calc_check_date(n, x, expected):
    assert JobAlert.calc_check_date(
        n, x) == datetime.strptime(expected, "%Y-%m-%d").date()
