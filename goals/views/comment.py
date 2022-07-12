from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.pagination import LimitOffsetPagination
from goals.models import GoalComment
from goals.permissions import CommentsPermissions
from goals.serializer import CommentSerializer, CommentCreateSerializer


class CommentListView(ListAPIView):
    model = GoalComment
    serializer_class = CommentSerializer
    permission_classes = [CommentsPermissions]
    pagination_class = LimitOffsetPagination
    filter_backends = [
        OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = ['goal']
    ordering = ["-id"]

    def get_queryset(self):
        return GoalComment.objects.filter(goal__category__board__participants__user=self.request.user)


class CommentCreateView(CreateAPIView):
    model = GoalComment
    permission_classes = [CommentsPermissions]
    serializer_class = CommentCreateSerializer


class CommentView(RetrieveUpdateDestroyAPIView):
    model = GoalComment
    permission_classes = [CommentsPermissions]
    serializer_class = CommentSerializer

    def get_queryset(self):
        return GoalComment.objects.filter(goal__category__board__participants__user=self.request.user)