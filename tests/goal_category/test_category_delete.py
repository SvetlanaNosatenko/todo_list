import pytest


@pytest.mark.django_db
def test_category_delete(client, logged_user, category, board_participants):

    response = client.delete(f"/goals/goal_category/{category.id}",
                             content_type="application/json"
                             )

    assert response.status_code == 204
