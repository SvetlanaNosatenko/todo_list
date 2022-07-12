import pytest


@pytest.mark.django_db
def test_create_board(client, logged_user):

    expected_response = {
        'created': '2022-07-02T17:36:02.951064Z',
        'id': 1,
        'is_deleted': False,
        'title': 'create_board',
        'updated': '2022-07-02T17:36:02.951064Z'
    }

    data = {
        'created': '2022-07-02T17:36:02.951064Z',
        'is_deleted': False,
        'title': 'create_board',
        'updated': '2022-07-02T17:36:02.951064Z'
    }

    response = client.post("/goals/board/create",
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
