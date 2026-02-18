from rest_framework import serializers
from .models import StudentProfile, TeacherProfile, User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate

# Custom Login Serializer
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        phone = attrs.get("phone") 
        password = attrs.get("password")
        user = authenticate(phone=phone, password=password)
        if not user:
            raise serializers.ValidationError("Invalid phone number or password.")
        data = super().validate(attrs)
        data['user_id'] = user.id
        data['role'] = user.role
        return data

# Registration Serializer
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['full_name', 'phone', 'password', 'role', 'user_type', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['phone'],
            phone=validated_data['phone'],
            full_name=validated_data['full_name'],
            password=validated_data['password'],
            email=validated_data.get('email', ''),
            role=validated_data.get('role', 'student'),
            user_type=validated_data.get('user_type', 'online')
        )
        return user

class TeacherProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherProfile
        fields = '__all__'

class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = '__all__'

class TeacherProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherProfile
        fields = ['full_name', 'address', 'academic_documents']

class StudentProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = ['current_class', 'school_college', 'address']