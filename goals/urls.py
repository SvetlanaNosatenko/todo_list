from django.urls import path

from goals.views import category, goal, comments, board

urlpatterns = [
    path("goal_category/create", category.GoalCategoryCreateView.as_view()),
    path("goal_category/list", category.GoalCategoryListView.as_view()),
    path("goal_category/<pk>", category.GoalCategoryView.as_view()),
    path("goal/<pk>", goal.GoalView.as_view()),
    path("goal/list", goal.GoalListView.as_view()),
    path("goal/create", goal.GoalCreateView.as_view()),
    path("goal_comment/<pk>", comments.CommentView.as_view()),
    path("goal_comment/list", comments.CommentListView.as_view()),
    path("goal_comment/create", comments.CommentCreateView.as_view()),
    path("board/<pk>", board.BoardView.as_view()),
    path("board/list", board.BoardListView.as_view()),
    path("board/create", board.BoardCreateView.as_view()),

]