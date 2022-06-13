from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated


from goals.models import GoalComment
from goals.permissions import CommentsPermissions
from goals.serializer import CommentSerializer, CommentCreateSerializer


class CommentListView(ListAPIView):
    model = GoalComment
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = LimitOffsetPagination
    filter_backends = [
        OrderingFilter,
        # DjangoFilterBackend,
    ]
    # filterset_class = GoalDateFilter
    filterset_fields = ['goal']
    ordering = ["-id"]
    search_fields = ["title", "description"]

    def get_queryset(self):
        return GoalComment.objects.filter(goal__category__board__participants__user=self.request.user)

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()
        return instance


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