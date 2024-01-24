from rest_framework import permissions

from contents.models import Content
from .models import Course
from rest_framework.views import Request, View


class IsSuperUserOrParticipant(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        if request.user.is_superuser:
            return True
        return request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request: Request, view: View, obj: Course):
        return request.user.is_superuser or request.user in obj.students.all()


class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        return request.user.is_superuser


class IsAdminOrParticipantReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj: Content):
        return (
            request.method in permissions.SAFE_METHODS
            and request.user in obj.course.students.all()
            or request.user.is_superuser
        )
