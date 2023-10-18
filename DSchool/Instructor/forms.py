from django import forms
from .models import Planning

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class PlanningForm(forms.ModelForm):
    class Meta:
        model = Planning
        fields = ["student", "instructor", "date", "place"]
        date = forms.DateTimeField(
            widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            input_formats=['%Y-%m-%dT%H:%M'],
        )