from rest_framework import permissions

READ_REQS = ('OPTIONS', 'HEAD', 'GET')
WRITE_REQS = ('POST', 'PUT', 'DELETE')


class IsOwnerOrReadOnlyIfAuthenticated(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in READ_REQS:
            return request.user.is_authenticated
        elif request.method in WRITE_REQS:
            return obj.student == request.user
        else:
            return False