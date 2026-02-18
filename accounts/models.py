from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('moderator', 'Moderator'),
        ('editor', 'Editor'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    TYPE_CHOICES = (
        ('online', 'Online'),
        ('offline', 'Offline'),
    )
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')
    user_type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='online') # Online/Offline filter er jonno
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f"{self.username} ({self.role})"
    
class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile')
    bio = models.TextField(blank=True)
    education = models.CharField(max_length=255, blank=True)
    experience = models.IntegerField(default=0) # Years of experience
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    is_verified = models.BooleanField(default=False) # Admin approve korle true hobe

    def __str__(self):
        return f"Teacher: {self.user.username}"

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    current_class = models.CharField(max_length=50, blank=True)
    school_college = models.CharField(max_length=255, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return f"Student: {self.user.username}"