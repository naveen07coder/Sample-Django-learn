from django import forms

class FeedbackForm(forms.Form):

    title = forms.CharField(label='Title', max_length=40, widget=forms.TextInput(attrs={'class':'form-control'}))
    subject = forms.CharField(label='Sub des', max_length=200, widget=forms.Textarea(attrs={'class':'form-control'}))
    email = forms.CharField(label='email', max_length=200, widget=forms.Textarea(attrs={'class': 'form-control'}))
