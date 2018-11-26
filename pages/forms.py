from django import forms
from django.core.mail import send_mail


class SendMail(forms.Form):
    subject = forms.CharField(
        widget=forms.TextInput())

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'text-input'}))

    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': '8',
            'cols': '50'}))

    def send_email(self):
        cd = self.cleaned_data
        send_mail(cd['subject'], cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['alekseypovar@yandex.com'],)
