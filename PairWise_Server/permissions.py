from rest_framework import permissions
from PairWise_Server.models import Profile

READ_REQS = ('OPTIONS', 'HEAD', 'GET')
WRITE_REQS = ('POST', 'PUT', 'DELETE')


class IsNotAuthenticated(permissions.BasePermission):
    """
    Only allow unauthenticated users to access an API endpoint, such as a login endpoint.
    """
    def has_permission(self, request, view):
        return not request.user.is_authenticated


class IsOwnerOrReadOnlyIfAuthenticated(permissions.BasePermission):
    """
    Users can only perform write operations (such as POST) to an API endpoint if they own the resource.
    Authenticated users who do not own the resource get read-only access (i.e. can perform GET request only).
    Unauthenticated users get no access to the endpoint.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in READ_REQS:
            return request.user.is_authenticated
        elif request.method in WRITE_REQS:
            return obj.student == request.user
        else:
            return False


class IsAuthenticatedAndHasProfile(permissions.BasePermission):
    """
    Users can only access a resource for read or write operations if they have created a profile and stored
    it in the database. Unauthenticated users or those who do not have a profile associated with their account
    are denied access to the endpoint.
    """
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        else:
            return Profile.objects.filter(student=request.user).exists()