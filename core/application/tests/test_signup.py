import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from application.models import CustomUser

@pytest.fixture
def ApiClient():
    # anonymous user
    client = APIClient()
    return client


@pytest.mark.django_db
class TestSignupByEmail():
    url = reverse('accounts:signup')

    """INVALID EMAIL"""
    def test_signup_invalid_email_response_400(self, ApiClient):
        # which are meant to be email
        
        # Case0: using whitespaces in email field
        response = ApiClient.post(self.url, data={
            "email": "testing whitespace@gmail.com",
            "username": "test-name",
            "password": "#normal-pass12345#",
            "password2": "#normal-pass12345#"
        })
        assert response.status_code == 400

        # Case1: no @ in input
        response = ApiClient.post(self.url, data={
            "email": "testingwhitespacegmail.com",
            "username": "test-name",
            "password": "#normal-pass12345#",
            "password2": "#normal-pass12345#"
        })
        assert response.status_code == 400

        # Case2: no . in input
        response = ApiClient.post(self.url, data={
            "email": "testingwhitespace@gmailcom",
            "username": "test-name",
            "password": "#normal-pass12345#",
            "password2": "#normal-pass12345#"
        })
        assert response.status_code == 400

        # Case3: no "com" in input
        response = ApiClient.post(self.url, data={
            "email": "testingwhitespacegmail.",
            "username": "test-name",
            "password": "#normal-pass12345#",
            "password2": "#normal-pass12345#"
        })
        assert response.status_code == 400
        
        # Case4: more than one @
        response = ApiClient.post(self.url, data={
            "email": "testingwhitespace@@gmail.com",
            "username": "test-name",
            "password": "#normal-pass12345#",
            "password2": "#normal-pass12345#"
        })
        assert response.status_code == 400

        # Case4: more than one .
        response = ApiClient.post(self.url, data={
            "email": "testingwhitespace@gmai.l.com",
            "username": "test-name",
            "password": "#normal-pass12345#",
            "password2": "#normal-pass12345#"
        })
        assert response.status_code == 400

        # Case5: more than one .
        response = ApiClient.post(self.url, data={
            "email": "testingwhitespace@gmai.l.com",
            "username": "test-name",
            "password": "#normal-pass12345#",
            "password2": "#normal-pass12345#"
        })
        assert response.status_code == 400

        # Case6: does not contain first part
        response = ApiClient.post(self.url, data={
            "email": "@gmail.com",
            "username": "test-name",
            "password": "#normal-pass12345#",
            "password2": "#normal-pass12345#"
        })
        assert response.status_code == 400

        # Case7: does not contain mid part
        response = ApiClient.post(self.url, data={
            "email": "testingmail@.com",
            "username": "test-name",
            "password": "#normal-pass12345#",
            "password2": "#normal-pass12345#"
        })
        assert response.status_code == 400

        # Case8: does not contain last part
        response = ApiClient.post(self.url, data={
            "email": "testingmail@gmail.",
            "username": "test-name",
            "password": "#normal-pass12345#",
            "password2": "#normal-pass12345#"
        })
        assert response.status_code == 400

    """VALID EMAIL"""
    def test_signup_valid_email_response_201(self, ApiClient):
        # which are meant to be email

        # Case0: standard gmail address
        response = ApiClient.post(self.url, data={
            "email": "testing@gmail.com",
            "username": "test-name",
            "password": "#normal-pass12345#",
            "password2": "#normal-pass12345#",
            "phone": "09333333333",
        })
        assert response.status_code == 201
        # check if the email field is not empty
        user = CustomUser.objects.filter(email="testing@gmail.com")
        assert user.exists() == True