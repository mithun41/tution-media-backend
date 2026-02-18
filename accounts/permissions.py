from rest_framework import permissions

class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        # Role string-ta lower case-e check koro
        return bool(
            request.user and 
            request.user.is_authenticated and 
            str(request.user.role).lower() == 'admin'
        )
        


class IsVerifiedTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        # User login kora thakte hobe, role 'teacher' hote hobe ebong verified hote hobe
        return bool(
            request.user and 
            request.user.is_authenticated and 
            request.user.role == 'teacher' and 
            request.user.teacher_profile.is_verified
        )