#forms

from django import forms
class ContactForm(forms.Form):
    conatct_name=forms.CharField(label='Enter your name ',required=True)
    conatct_email=forms.EmailField(label='Enetr Email id',required=True)
    message=forms.CharField(label='your message',required=True,widget=forms.Textarea)
