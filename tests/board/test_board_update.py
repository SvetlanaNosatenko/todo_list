from http import HTTPStatus

import pytest

from goals.serializer import BoardSerializer


@pytest.mark.django_db
def test_board_update(client, logged_user, board, board_participants):
    expected_response = BoardSerializer(board).data
    expected_response["title"] = "updated_board"

    response = client.patch(f"/goals/board/{board.id}",
                            {"title": "updated_board"},
                            content_type="application/json"
                            )

    response_json = response.json()
    response_json.pop("updated")
    expected_response.pop("updated")

    assert response.status_code == HTTPStatus.OK
    assert response_json == expected_response
