import pytest
#
# from core.models import User
#
#
# @pytest.fixture()
# @pytest.mark.django_db
# def user(client):
#     # username = "username_test"
#     # password = "password"
#     # email = "email"
#
#     return User.objects.create_user(
#         username="username",
#         password="password",
#         email="email",
#         first_name="name_test",
#         last_name="last_name_test",
#         is_staff=False,
#         is_superuser=False,
#         is_active=True,
#     )

    # response = client.post(
    #     "/core/login/",
    #     {"username": username, "password": password, "email": email}, format="json"
    # )
    # return response.data["access"]
#
# @pytest.fixture()
# @pytest.mark.django_db
# def logged_user(client, user):
#     client.login(username=user.username, password="password")
#     return user
