from django.contrib import admin
from .models import Student, Instructor, Planning

class PlanningAdmin(admin.ModelAdmin):
    list_display = ["student", "instructor", "date", "place", "hour"]
    list_filter = ["date"]
    search_fields = ["student", "instructor", "date"]

admin.site.register(Student)
admin.site.register(Instructor)
admin.site.register(Planning, PlanningAdmin)

# Register your models here.
