from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.models import TeacherProfile, User, StudentProfile
from accounts.permissions import IsAdminUser, IsVerifiedTeacher
from .serializers import RegisterSerializer, StudentProfileSerializer, TeacherProfileSerializer
from rest_framework.permissions import AllowAny
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from .serializers import TeacherProfileUpdateSerializer, StudentProfileUpdateSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class ProfileUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = self.request.user
        if user.role == 'teacher':
            # hasattr use kora safe practice
            return getattr(user, 'teacher_profile', None)
        elif user.role == 'student':
            return getattr(user, 'student_profile', None)
        return None

    def get_serializer_class(self):
        # Role onujayi alada serializer choose korbe
        if self.request.user.role == 'teacher':
            return TeacherProfileUpdateSerializer
        return StudentProfileUpdateSerializer

    def patch(self, request, *args, **kwargs):
        profile = self.get_object()
        if not profile:
            return Response({"error": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.get_serializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


# Admin shob teacher-der list dekhte parbe
class AdminTeacherListView(generics.ListAPIView):
    queryset = TeacherProfile.objects.all()
    serializer_class = TeacherProfileSerializer
    permission_classes = [IsAdminUser]
    # search_fields ba filter_backends ekhane add kora jabe

# Admin shob student-der list dekhte parbe
class AdminStudentListView(generics.ListAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer
    permission_classes = [IsAdminUser]
    


class AdminVerifyTeacherView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request, pk):
        try:
            teacher = TeacherProfile.objects.get(pk=pk)
            # Toggle verification status
            teacher.is_verified = not teacher.is_verified
            teacher.save()
            return Response({"status": "success", "is_verified": teacher.is_verified})
        except TeacherProfile.DoesNotExist:
            return Response({"error": "Teacher not found"}, status=404)
        
class TeacherProfileSubmitView(generics.UpdateAPIView):
    serializer_class = TeacherProfileUpdateSerializer # Age banano serializer-e field gulo add kore nio
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.teacher_profile

    def perform_update(self, serializer):
        # Form submit korle is_submitted True hoye jabe
        serializer.save(is_submitted=True)

class TeacherDashboardView(APIView):
    permission_classes = [IsVerifiedTeacher]

    def get(self, request):
        return Response({
            "message": "Welcome to Teacher Dashboard!",
            "data": "Only verified teachers can see this."
        })