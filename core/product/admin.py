from django.contrib import admin
from .models import Student, Course, HighSchoolMajor
from .forms import StudentForm, HighSchoolMajorForm

class CourseAdmin(admin.ModelAdmin):
    pass

class HighSchoolMajorAdmin(admin.ModelAdmin):
    form = HighSchoolMajorForm

class StudentAdmin(admin.ModelAdmin):
    form = StudentForm
    
admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(HighSchoolMajor, HighSchoolMajorAdmin)

