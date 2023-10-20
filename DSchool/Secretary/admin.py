from django.contrib import admin
from .models import Student, Instructor, Planning, Secretary

class PlanningAdmin(admin.ModelAdmin):
    list_display = ["student", "instructor", "date", "place"]
    list_filter = ["date"]
    search_fields = ["student", "instructor", "date"]

class StudentAdmin(admin.ModelAdmin):
    list_display = ["username", "password", "h_total", "h_remaining"]
    list_filter = ["h_remaining"]
    search_fields = ["username"]

class InstructorAdmin(admin.ModelAdmin):
    list_display = ["username", "password","name","lastname"]
    search_fields = ["username"]

class SecretaryAdmin(admin.ModelAdmin):
    list_display = ["username", "password"]
    search_fields = ["username"]

admin.site.register(Student, StudentAdmin)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Planning, PlanningAdmin)
admin.site.register(Secretary, SecretaryAdmin)
# Register your models here.
