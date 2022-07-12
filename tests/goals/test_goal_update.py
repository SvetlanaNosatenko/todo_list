from http import HTTPStatus
import pytest
from goals.serializer import GoalSerializer


@pytest.mark.django_db
def test_category_update(client, logged_user, goal, board_participants):
    expected_response = GoalSerializer(goal).data
    expected_response["title"] = "updated_goal"

    response = client.patch(f"/goals/goal/{goal.id}",
                            {"title": "updated_goal"},
                            content_type="application/json"
                            )

    response_json = response.json()
    response_json.pop("updated")
    expected_response.pop("updated")

    assert response.status_code == HTTPStatus.OK
    assert response_json == expected_response