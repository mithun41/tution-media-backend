from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import AdminVerifyTeacherView, ProfileUpdateView, RegisterView, AdminTeacherListView, AdminStudentListView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile_update'),
    path('admin/teachers/', AdminTeacherListView.as_view(), name='admin_teacher_list'),
    path('admin/students/', AdminStudentListView.as_view(), name='admin_student_list'),
    path('admin/teacher-verify/<int:pk>/', AdminVerifyTeacherView.as_view(), name='admin_teacher_verify'),
]
