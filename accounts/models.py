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
    full_name = models.CharField(max_length=255) 
    phone = models.CharField(max_length=15, unique=True)
    
    USERNAME_FIELD = 'phone' # Login hobe phone number diye
    REQUIRED_FIELDS = ['username'] # Database logic-er jonno thakbe

    def __str__(self):
        return f"{self.full_name} ({self.phone})"
    
class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile')
    full_name = models.CharField(max_length=255, blank=True)
    address = models.TextField(blank=True)
    academic_documents = models.FileField(upload_to='teacher_docs/', blank=True, null=True)
    is_verified = models.BooleanField(default=False) # Eita Admin control korbe
    is_submitted = models.BooleanField(default=False) # Teacher form fillup korle True hobe

    def __str__(self):
        return self.user.username

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    current_class = models.CharField(max_length=50, blank=True)
    school_college = models.CharField(max_length=255, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return f"Student: {self.user.username}"