import pytest


@pytest.mark.django_db
def test_create_category(client, logged_user, board, board_participants_1):

    expected_response = {
        "id": 6,
        "board": board.id,
        "title": "title_category",
        "is_deleted": False
    }

    data = {
        "board": board.id,
        "title": "title_category",
        "is_deleted": False
    }

    response = client.post("/goals/goal_category/create",
                           data,
                           content_type="application/json"
                           )
    response_json = response.json()
    response_json.pop("updated")
    response_json.pop("created")

    assert response.status_code == 201
    assert response_json == expected_response

