import pytest


@pytest.mark.django_db
def test_create_user(client):

    expected_response = {
        "id": 21,
        "first_name": "first_name",
        "last_name": "last_name",
        "email": "test@mail.ru",
        "username": "username"
     }

    data = {
        "password": "password_test",
        "username": "username",
        "first_name": "first_name",
        "last_name": "last_name",
        "email": "test@mail.ru",
        "password_repeat": "password_test"
    }

    response = client.post("/core/signup",
                           data,
                           content_type="application/json"
                           )

    assert response.status_code == 201
    assert response.data == expected_response
