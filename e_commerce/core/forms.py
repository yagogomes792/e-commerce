from django import forms

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