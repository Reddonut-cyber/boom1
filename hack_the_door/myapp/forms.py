from django import forms

class StringForm(forms.Form):
    input_string = forms.CharField(label='Enter your string', max_length=100)
