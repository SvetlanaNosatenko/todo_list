import pytest


@pytest.mark.django_db
def test_create_comment(client, logged_user, goal, board_participants):

    expected_response = {
        'created': '2022-07-02T17:36:02.951064Z',
        'goal': goal.pk,
        'id': 6,
        'text': 'text_test',
        'updated': '2022-07-02T17:36:02.951064Z'
    }

    data = {
        'goal': goal.pk,
        'text': 'text_test'
    }

    response = client.post("/goals/goal_comment/create",
                           data,
                           content_type="application/json"
                           )

    response_json = response.json()
    response_json.pop("updated")
    expected_response.pop("updated")
    response_json.pop("created")
    expected_response.pop("created")

    assert response.status_code == 201
    assert response_json == expected_response