from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from goals.filters import GoalDateFilter
from goals.models import GoalComment
from goals.permissions import CommentsPermissions
from goals.serializers import CommentCreateSerializer, CommentSerializer


# class GoalCommentListView(ListAPIView):
#     model = GoalComment
#     permission_classes = [IsAuthenticated]
#     serializer_class = CommentSerializer
#     pagination_class = LimitOffsetPagination
#     filter_backends = [
#         DjangoFilterBackend,
#         OrderingFilter,
#         SearchFilter,
#     ]
#     filterset_class = GoalDateFilter
#     ordering_fields = ["due_date", 'priority']
#     ordering = ["title"]
#     search_fields = ["title", "description"]
#
#     def get_queryset(self):
#         return Goal.objects.filter(user=self.request.user, is_deleted=False)


class CommentListView(ListAPIView):
    model = GoalComment
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, CommentsPermissions]
    pagination_class = LimitOffsetPagination
    filter_backends = [
        OrderingFilter,
        DjangoFilterBackend,
    ]
    # filterset_class = GoalDateFilter
    filterset_fields = ['goal']
    ordering = ["-id"]
    # search_fields = ["title", "description"]

    def get_queryset(self):
        return GoalComment.objects.filter(goal__category__board__participants__user=self.request.user)

    # def perform_destroy(self, instance):
    #     instance.is_deleted = True
    #     instance.save()
    #     return instance


class CommentCreateView(CreateAPIView):
    model = GoalComment
    permission_classes = [IsAuthenticated, CommentsPermissions]
    serializer_class = CommentCreateSerializer


class CommentView(RetrieveUpdateDestroyAPIView):
    model = GoalComment
    permission_classes = [IsAuthenticated, CommentsPermissions]
    serializer_class = CommentSerializer

    def get_queryset(self):
        return GoalComment.objects.filter(goal__category__board__participants__user=self.request.user)