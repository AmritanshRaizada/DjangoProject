from django import forms
from .models import Student
from .models import Teacher

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'email']
        exclude = ['created_at']
class TeacherForm(forms.ModelForm):
    class Meta:
        model=Teacher
        fields = ['name', 'age', 'email']
