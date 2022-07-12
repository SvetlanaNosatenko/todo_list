from http import HTTPStatus
import pytest
from goals.serializer import CommentSerializer


@pytest.mark.django_db
def test_comment_detail(client, logged_user, comment, board_participants):

    response = client.get(f"/goals/goal_comment/{comment.id}",
                          content_type="application/json"
                          )

    assert response.status_code == HTTPStatus.OK
    assert response.data == CommentSerializer(comment).data

