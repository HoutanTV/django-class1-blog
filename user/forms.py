from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    birthday = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'birthday', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'




# class UserRegisterForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['email', 'username', 'first_name', 'last_name', 'birthday', 'password']
#         widgets = {
#             'email': forms.EmailInput(attrs={'class': 'form-control'}),
#             'username': forms.TextInput(attrs={'class': 'form-control'}),
#             'first_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'last_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'birthday': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
#             'password': forms.PasswordInput(attrs={'class': 'form-control'}),
#         }
