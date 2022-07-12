import pytest


@pytest.mark.django_db
def test_goal_delete(client, logged_user, goal, board_participants):

    response = client.delete(f"/goals/goal/{goal.id}",
                             content_type="application/json"
                             )

    assert response.status_code == 204