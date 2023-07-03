from django import forms
from .models import Student, Course,HighSchoolMajor

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'family_name', 'national_id', 'high_school_major', 'courses']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['courses'].queryset = Course.objects.none()

        if 'high_school_major' in self.data:
            try:
                high_school_major_id = int(self.data.get('high_school_major'))
                self.fields['courses'].queryset = Course.objects.filter(high_school_major_id=high_school_major_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['courses'].queryset = self.instance.high_school_major.course_set

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name']

class HighSchoolMajorForm(forms.ModelForm):
    class Meta:
        model = HighSchoolMajor
        fields = ['name']
