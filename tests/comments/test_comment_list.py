import pytest


@pytest.mark.django_db
def test_comment_list(client, logged_user, board_participants, goal, comment, comment_1):
    response = client.get("/goals/goal_comment/list")

    expected_response = [
        {
            'goal': goal.id,
            'id': comment_1.id,
            'text': comment_1.text
        },
        {
            'goal': goal.id,
            'id': comment.id,
            'text': comment.text
        }
    ]

    response_json = response.json()
    for resp in response_json:
        resp.pop("updated")
        resp.pop("created")

    assert response.status_code == 200
    assert response_json == expected_response
