from http import HTTPStatus
import pytest
from goals.serializer import GoalSerializer


@pytest.mark.django_db
def test_goal_detail(client, logged_user, goal, board_participants):

    response = client.get(f"/goals/goal/{goal.id}",
                          content_type="application/json"
                          )

    assert response.status_code == HTTPStatus.OK
    assert response.data == GoalSerializer(goal).data