"""
Forms for the webSite app
"""
from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import SetPasswordForm


class ConnexionForm(forms.Form):
    """
    Form for the connexion
    """
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(
        label="Mot de passe", widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    """
    Form for the account registration
    """
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(
        label="Mot de passe", widget=forms.PasswordInput)
    email = forms.EmailField(label="Addresse mail", required=True)


class SetPasswordFormFR(SetPasswordForm):
    """
    A form that lets a user change set their password without entering the old
    password
    """
    error_messages = {
        'password_mismatch': ("The two password fields didn't match."),
    }
    new_password1 = forms.CharField(
        label=("Nouveau mot de passe"),
        widget=forms.PasswordInput,
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=("Confirmation du nouveau mot de passe"),
        strip=False,
        widget=forms.PasswordInput,
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )
        password_validation.validate_password(password2, self.user)
        return password2

    def save(self, commit=True):
        password = self.cleaned_data["new_password1"]
        self.user.set_password(password)
        if commit:
            self.user.save()
        return self.user
