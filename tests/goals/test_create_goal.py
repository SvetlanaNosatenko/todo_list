import pytest


@pytest.mark.django_db
def test_create_goal(client, logged_user):
    expected_response = {
        "id": 1,
        "title": "name_number_1",
        "description": "description",
        # "category": goal.id,
        "status": 1,
        "priority": 3,
        "due_date": None,
        "user": logged_user.id,
    }
    data = {
        "id": 1,
        "title": "name_number_1",
        "description": "description",
        # "category": goal.id,
        "status": 1,
        "priority": 3,
        "due_date": None,
        "user": logged_user.id,
    }

    response = client.post("/goal/create/",
                           data,
                           content_type="application/json"
                           )
    assert response.status_code == 201
    assert response.data == expected_response
