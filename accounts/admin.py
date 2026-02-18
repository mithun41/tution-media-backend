from django.contrib import admin
from .models import User, TeacherProfile, StudentProfile

admin.site.register(User)

@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
    # Ekhane experience field-ta thaka jabe na
    list_display = ['user', 'full_name', 'is_verified', 'is_submitted']
    list_filter = ['is_verified', 'is_submitted']
    actions = ['approve_teachers']

    def approve_teachers(self, request, queryset):
        queryset.update(is_verified=True)
    approve_teachers.short_description = "Approve selected teachers"

admin.site.register(StudentProfile)