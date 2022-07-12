import pytest


@pytest.mark.django_db
def test_comment_delete(client, logged_user, comment, board_participants_1):

    response = client.delete(f"/goals/goal_comment/{comment.id}",
                             content_type="application/json"
                             )

    assert response.status_code == 204