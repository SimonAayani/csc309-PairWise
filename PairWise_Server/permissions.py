from rest_framework import permissions
from PairWise_Server.models import Profile

READ_REQS = ('OPTIONS', 'HEAD', 'GET')
WRITE_REQS = ('POST', 'PUT', 'DELETE')


class IsNotAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        return not request.user.is_authenticated


class IsOwnerOrReadOnlyIfAuthenticated(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in READ_REQS:
            return request.user.is_authenticated
        elif request.method in WRITE_REQS:
            return obj.student == request.user
        else:
            return False


class IsAuthenticatedAndHasProfile(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        else:
            return Profile.objects.filter(student=request.user).exists()