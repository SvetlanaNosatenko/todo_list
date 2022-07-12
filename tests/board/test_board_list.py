import pytest


@pytest.mark.django_db
def test_list_board(client, logged_user, board_participants_2, board_participants_1, board_1, board):

    response = client.get("/goals/board/list")

    expected_response = [
        {
            "id": board.id,
            'is_deleted': False,
            'title': board.title
        },
        {
            "id": board_1.id,
            'is_deleted': False,
            'title': board_1.title
        }
    ]

    response_json = response.json()
    for resp in response_json:
        resp.pop("updated")
        resp.pop("created")
    # for resp_exp in expected_response:
    #     resp_exp.pop("updated")
    #     resp_exp.pop("created")

    assert response.status_code == 200
    assert response_json == expected_response
