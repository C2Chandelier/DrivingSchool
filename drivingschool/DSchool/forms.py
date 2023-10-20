from django import forms
from .models import Student, Planning

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['username', 'password', 'h_total'] 


class AddPlanningForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Date'  # Étiquette du champ
    )

    class Meta:
        model = Planning
        fields = ['instructor', 'date', 'place']