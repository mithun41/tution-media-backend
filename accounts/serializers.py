from rest_framework import serializers
from .models import StudentProfile, TeacherProfile, User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role', 'user_type', 'phone']

    def create(self, validated_data):
        # Shudhu Teacher ba Student register korte parbe
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password'],
            role=validated_data.get('role', 'student'),
            user_type=validated_data.get('user_type', 'online'),
            phone=validated_data.get('phone', '')
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
        # Admin verification chara baki field teacher update korte parbe
        fields = ['bio', 'education', 'experience', 'hourly_rate']

class StudentProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = ['current_class', 'school_college', 'address']