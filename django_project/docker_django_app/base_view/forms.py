from django import forms

class NameForm(forms.Form):
    user_name = forms.CharField(max_length = 30)