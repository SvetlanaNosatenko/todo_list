from http import HTTPStatus
import pytest
from goals.serializer import GoalCategorySerializer


@pytest.mark.django_db
def test_category_update(client, logged_user, category, board_participants):
    expected_response = GoalCategorySerializer(category).data
    expected_response["title"] = "updated_category"

    response = client.patch(f"/goals/goal_category/{category.id}",
                            {"title": "updated_category"},
                            content_type="application/json"
                            )

    response_json = response.json()
    response_json.pop("updated")
    expected_response.pop("updated")

    assert response.status_code == HTTPStatus.OK
    assert response_json == expected_response

