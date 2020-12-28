import pytest
from django.contrib.auth.models import User
from .models import UserAccount


@pytest.fixture
def user_account(db):
    """test account to reduce redundancy"""
    username = 'testuser'
    password = 'lvkmdgv32fdbf1b'
    email = 'testuser@test.com'
    new_user = User.objects.create_user(
        username=username, password=password, email=email
    )
    return new_user


@pytest.mark.django_db()
def test_user_create(user_account):
    """Create a user and check if a UserAccount instance was created"""
    assert UserAccount.objects.get(user=user_account)


@pytest.mark.django_db()
def test_user_find(user_account):
    """Find user in database"""
    assert User.objects.get(username=user_account.username)
