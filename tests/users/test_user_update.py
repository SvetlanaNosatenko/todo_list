from http import HTTPStatus
import pytest
from core.serializers import UpdatePasswordSerializer


@pytest.mark.django_db
def test_user_update(client, logged_user, board_participants):
    expected_response = UpdatePasswordSerializer(logged_user).data

    response = client.patch("/core/update_password",
                            {"new_password": "new_password",
                             "old_password": "password_test"
                             },
                            content_type="application/json"
                            )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == expected_response