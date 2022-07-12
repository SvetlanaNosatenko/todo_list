from http import HTTPStatus
import pytest
from goals.serializer import CommentSerializer


@pytest.mark.django_db
def test_comment_update(client, logged_user, comment, board_participants):
    expected_response = CommentSerializer(comment).data
    expected_response["text"] = "updated_comment"

    response = client.patch(f"/goals/goal_comment/{comment.id}",
                            {"text": "updated_comment"},
                            content_type="application/json"
                            )

    response_json = response.json()
    response_json.pop("updated")
    expected_response.pop("updated")

    assert response.status_code == HTTPStatus.OK
    assert response_json == expected_response