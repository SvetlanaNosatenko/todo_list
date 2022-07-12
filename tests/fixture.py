import pytest
from goals.models import Board, BoardParticipant, GoalCategory, Goal, GoalComment


@pytest.fixture()
@pytest.mark.django_db
def user(client, django_user_model):
    return django_user_model.objects.create_user(
        username="username_test",
        password="password_test"
    )


@pytest.fixture()
@pytest.mark.django_db
def logged_user(client, user):
    client.login(username=user.username, password="password_test")
    return user


@pytest.fixture()
@pytest.mark.django_db
def board(client):
    board = "board_title"
    return Board.objects.create(title=board)


@pytest.fixture()
@pytest.mark.django_db
def board_1(client):
    board_1 = "board_title_1"
    return Board.objects.create(title=board_1)


@pytest.fixture()
@pytest.mark.django_db
def board_participants(client, board, user):
    return BoardParticipant.objects.create(board=board, user=user)


@pytest.fixture()
@pytest.mark.django_db
def board_participants_1(client, board, user):
    return BoardParticipant.objects.create(board=board, user=user, role=1)


@pytest.fixture()
@pytest.mark.django_db
def board_participants_2(client, board_1, user):
    return BoardParticipant.objects.create(board=board_1, user=user, role=1)


@pytest.fixture()
@pytest.mark.django_db
def category(client, board, user):
    category = "category_title"
    return GoalCategory.objects.create(title=category, board=board, user=user)


@pytest.fixture()
@pytest.mark.django_db
def category_1(client, board, user):
    category_1 = "category_title_1"
    return GoalCategory.objects.create(title=category_1, board=board, user=user)


@pytest.fixture()
@pytest.mark.django_db
def goal(client, category, user):
    goal = "goal_title"
    return Goal.objects.create(title=goal, category=category, user=user)


@pytest.fixture()
@pytest.mark.django_db
def goal_1(client, category, user):
    goal_1 = "goal_title_1"
    return Goal.objects.create(title=goal_1, category=category, user=user)


@pytest.fixture()
@pytest.mark.django_db
def comment(client, goal):
    comment = "comment_test"
    return GoalComment.objects.create(text=comment, goal=goal)


@pytest.fixture()
@pytest.mark.django_db
def comment_1(client, goal):
    comment_1 = "comment_test_1"
    return GoalComment.objects.create(text=comment_1, goal=goal)
