from django import forms

class MessageForm(forms.Form):
    text = forms.CharField(label='Текст',widget=forms.TextInput(attrs={'class': 'form-control'}))
