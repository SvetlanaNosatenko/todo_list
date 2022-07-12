from http import HTTPStatus

import pytest

from goals.serializer import GoalCategorySerializer


@pytest.mark.django_db
def test_category_detail(client, logged_user, category, board_participants):

    response = client.get(f"/goals/goal_category/{category.id}",
                          content_type="application/json"
                          )

    assert response.status_code == HTTPStatus.OK
    assert response.data == GoalCategorySerializer(category).data

