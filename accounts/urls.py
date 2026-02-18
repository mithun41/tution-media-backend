from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    AdminVerifyTeacherView, ProfileUpdateView, RegisterView, 
    AdminTeacherListView, AdminStudentListView, TeacherDashboardView, 
    TeacherProfileSubmitView
)
# Custom serializer ta import koro jeta serializers.py te banano hoyeche
from .serializers import CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# Custom view banacchi jate JWT amader phone number wala logic use kore
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

urlpatterns = [
    # --- Authentication ---
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'), # Updated here
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # --- Profile & Dashboard ---
    path('profile/update/', ProfileUpdateView.as_view(), name='profile_update'),
    path('teacher/submit-profile/', TeacherProfileSubmitView.as_view(), name='teacher_submit_profile'),
    path('teacher/dashboard/', TeacherDashboardView.as_view(), name='teacher_dashboard'),
    
    # --- Admin Controls ---
    path('admin/teachers/', AdminTeacherListView.as_view(), name='admin_teacher_list'),
    path('admin/students/', AdminStudentListView.as_view(), name='admin_student_list'),
    path('admin/teacher-verify/<int:pk>/', AdminVerifyTeacherView.as_view(), name='admin_teacher_verify'),
]