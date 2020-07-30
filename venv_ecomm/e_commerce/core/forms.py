from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()
class ContactForm(forms.Form):
    fullname = forms.CharField(
        error_messages={'required': 'Éobrigatório o preenchimento do nome completo'},
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite seu nome completo'
            }
        )
    )
    email = forms.EmailField(
        error_messages={'invalid': 'Digite um e-mail válido'},
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite seu e-mail'
            }
        )
    )
    content = forms.CharField(
        error_messages={'required': 'É obrigatório escrever uma mensagem'},
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua mensagem'
            }
        )
    )

class LoginForm(forms.Form):
        username = forms.CharField()
        password = forms.CharField(widget=forms.PasswordInput)
    
class RegisterForm(forms.Form):
        username = forms.CharField()
        email = forms.EmailField()
        password = forms.CharField(widget=forms.PasswordInput)
        password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    
        def clean_username(self):
            username = self.cleaned_data.get('username')
            qs = User.objects.filter(username=username)
            if qs.exists():
                raise forms.ValidationError('Esse usuário já existe, escolha outro.')
            return username
        
        def clean_email(self):
            email = self.cleaned_data.get('email')
            qs = User.objects.filter(email=email)
            if qs.exists():
                raise forms.ValidationError('Esse e-mail já existe, escolha outro e-mail.')
            return email
        
        def clean(self):
            data = self.cleaned_data
            password = self.cleaned_data.get('password')
            password2 = self.cleaned_data.get('password2')
            if password != password2:
                raise forms.ValidationError('As senhas devem ser iguais')
            return data
    