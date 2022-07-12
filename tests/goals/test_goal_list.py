import pytest


@pytest.mark.django_db
def test_list_goal(client, logged_user, board_participants, goal, goal_1, category):
    response = client.get("/goals/goal/list")

    expected_response = [
        {
            "id": goal.id,
            "title": goal.title,
            "description": goal.description,
            "category": category.id,
            "status": 1,
            "priority": 2,
            "due_date": None,
            'user': {'email': logged_user.email,
                     'first_name': logged_user.first_name,
                     'id': logged_user.id,
                     'last_name': logged_user.last_name,
                     'username': 'username_test'}
        },
        {
            "id": goal_1.id,
            "title": goal_1.title,
            "description": goal_1.description,
            "category": category.id,
            "status": 1,
            "priority": 2,
            "due_date": None,
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
