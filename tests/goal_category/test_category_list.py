import pytest


@pytest.mark.django_db
def test_list_category(client, logged_user, board_participants, category, board, category_1):
    response = client.get("/goals/goal_category/list")

    expected_response = [
        {
            "id": category.id,
            "board": board.id,
            "title": category.title,
            "is_deleted": False,
            'user': {'email': logged_user.email,
                     'first_name': logged_user.first_name,
                     'id': logged_user.id,
                     'last_name': logged_user.last_name,
                     'username': 'username_test'}
        },
        {
            "id": category_1.id,
            "board": board.id,
            "title": category_1.title,
            "is_deleted": False,
            'user': {'email': logged_user.email,
                     'first_name': logged_user.first_name,
                     'id': logged_user.id,
                     'last_name': logged_user.last_name,
                     'username': 'username_test'}
        }
    ]

    response_json = response.json()
    for resp in response_json:
        resp.pop("updated")
        resp.pop("created")

    assert response.status_code == 200
    assert response_json == expected_response
