import pytest


@pytest.mark.django_db
def test_board_delete(client, logged_user, board, board_participants):

    response = client.delete(f"/goals/board/{board.id}",
                             content_type="application/json"
                             )

    assert response.status_code == 204

