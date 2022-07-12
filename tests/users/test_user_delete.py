import pytest


@pytest.mark.django_db
def test_user_delete(client, logged_user, board_participants):

    response = client.delete("/core/profile",
                             content_type="application/json"
                             )

    assert response.status_code == 204