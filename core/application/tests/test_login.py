import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from application.models import CustomUser

@pytest.fixture
def ApiClient():
    # anonymous user
    client = APIClient()
    return client

@pytest.fixture
def CommonUser():
    user = CustomUser.objects.create_user(
        username = 'test-email',
        email = 'testing@gmail.com',
        password ='#correct-pass12345#',
        phone = '09111111111'
    )
    return user

@pytest.mark.django_db
class TestLoginEmail():
    url = reverse('accounts:login')

    def test_login_not_registered_email_response_404(self, ApiClient , CommonUser):
        # user is not registered and wont be found (404)
        response = ApiClient.post(self.url, data={
                "email": "testing_@gmail.com",
                "password": "#failed-pass12345#",
            })
        assert response.status_code == 404

    def test_login_correct_email_response_200(self, ApiClient , CommonUser):
        response = ApiClient.post(self.url, data={
                "email": 'testing@gmail.com',
                "password": "#correct-pass12345#"
            })
        assert response.status_code == 200