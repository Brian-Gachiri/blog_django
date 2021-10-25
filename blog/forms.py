from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    email = forms.EmailField(max_length=100)
    phone_number = forms.CharField(widget = forms.NumberInput)
    message = forms.CharField(widget = forms.Textarea)

class MailForm(forms.Form):
    subject = forms.CharField(max_length=200)
    recipient = forms.EmailField(max_length = 100)
    message = forms.CharField(widget = forms.Textarea)
