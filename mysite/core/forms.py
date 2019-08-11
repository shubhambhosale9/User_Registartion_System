from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from .models import User
CHOICES= [
    ('YES', 'YES'),
    ('NO', 'NO'),
    ]

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=False)
    web_address = forms.CharField(max_length=30, required=False)
    cover_letter = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    file = forms.FileField()
    work_choice = forms.CharField(label='Do you like working?', widget=forms.Select(choices=CHOICES))
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('username', 'email',  'password1', 'password2', 'web_address', 'cover_letter', 'work_choice', 'file')

    def save(self, commit =True):
        user = super(SignUpForm, self).save(commit=False)
        user.name = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.web_address = self.cleaned_data['web_address']
        user.cover_letter = self.cleaned_data['cover_letter']
        user.work_choice = self.cleaned_data['work_choice']
        user.file = self.cleaned_data.get('file')

        if commit:
            user.save()
