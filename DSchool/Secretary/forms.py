from django import forms
from .models import Planning
from Student.models import Student
from Instructor.models import Instructor

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['username', 'password', 'h_total'] 

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ['username', 'password'] 


class AddPlanningForm(forms.ModelForm):
    class Meta:
        model = Planning
        fields = ['instructor', 'date', 'place']

class AddPlanningFormInstructor(forms.ModelForm):
    class Meta:
        model = Planning
        fields = ['student', 'date', 'place']

class PlanningFormModif(forms.ModelForm):
    class Meta:
        model = Planning
        fields = [ "date", "place"]
        date = forms.DateTimeField(
            widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            input_formats=['%Y-%m-%dT%H:%M'],
        )    
