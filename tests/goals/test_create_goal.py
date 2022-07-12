import pytest


@pytest.mark.django_db
def test_create_goal(client, logged_user, category, board_participants_1):

    expected_response = {
        "id": 6,
        "title": "title",
        "description": "description",
        "category": category.id,
        "status": 1,
        "priority": 2,
        "due_date": None
    }

    data = {
        "title": "title",
        "description": "description",
        "user": logged_user.id,
        "category": category.id,
        "status": 1,
        "priority": 2
    }

    response = client.post("/goals/goal/create",
                           data,
                           content_type="application/json"
                           )

    response_json = response.json()
    response_json.pop("updated")
    response_json.pop("created")

    assert response.status_code == 201
    assert response_json == expected_response

