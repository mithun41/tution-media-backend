from rest_framework import permissions

class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        # Role string-ta lower case-e check koro
        return bool(
            request.user and 
            request.user.is_authenticated and 
            str(request.user.role).lower() == 'admin'
        )