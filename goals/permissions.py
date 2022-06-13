from rest_framework import permissions

from goals.models import BoardParticipant


class BoardPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False

        if request.method in permissions.SAFE_METHODS:
            return BoardParticipant.objects.filter(
                user=request.user, board=obj
            ).exists()
        return BoardParticipant.objects.filter(
            user=request.user, board=obj, role=BoardParticipant.Role.OWNER
        ).exists()


class GoalCategoryPermissions(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False

        filters: dict = {'user': request.user, 'board': obj.board}
        if request.method not in permissions.SAFE_METHODS:
            filters['role__in'] = [BoardParticipant.Role.OWNER, BoardParticipant.Role.WRITER]

        return BoardParticipant.objects.filter(**filters).exists()


class GoalPermissions(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False

        filters: dict = {'user': request.user, 'board': obj.category.board}
        if request.method not in permissions.SAFE_METHODS:
            filters['role__in'] = [BoardParticipant.Role.OWNER, BoardParticipant.Role.WRITER]

        return BoardParticipant.objects.filter(**filters).exists()


class CommentsPermissions(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user