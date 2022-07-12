from http import HTTPStatus
import pytest
from goals.serializer import BoardSerializer


@pytest.mark.django_db
def test_board_detail(client, logged_user, board, board_participants):

    response = client.get(f"/goals/board/{board.id}",
                          content_type="application/json"
                          )

    assert response.status_code == HTTPStatus.OK
    assert response.data == BoardSerializer(board).data
