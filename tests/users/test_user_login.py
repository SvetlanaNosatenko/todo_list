from http import HTTPStatus
import pytest
from core.serializers import LoginSerializer


@pytest.mark.django_db
def test_user_login(client, user):
    expected_response = LoginSerializer(user).data

    response = client.post("/core/login",
                           {"password": "password_test",
                            "username": "username_test"},
                           content_type="application/json"
                           )

    assert response.status_code == HTTPStatus.OK
    assert response.data == expected_response
