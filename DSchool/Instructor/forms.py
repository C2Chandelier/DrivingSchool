from django import forms
from Secretary.models import Planning

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class PlanningFormAdd(forms.ModelForm):
    class Meta:
        model = Planning
        fields = ["student", "date", "place"]
        date = forms.DateTimeField(
            widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            input_formats=['%Y-%m-%dT%H:%M'],
        )

class PlanningFormModif(forms.ModelForm):
    class Meta:
        model = Planning
        fields = [ "date", "place"]
        date = forms.DateTimeField(
            widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            input_formats=['%Y-%m-%dT%H:%M'],
        )        