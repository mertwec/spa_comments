from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginForm(AuthenticationForm):
    # username = forms.CharField(
    #     max_length=256,
    #     required=True,
    #     validators=[domen_name, email_name]
    # )
    class Meta:
        model = User
        fields = (
            'username',
            'password'
        )


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', "last_name", "first_name")


class ConfForm(forms.ModelForm):
    secret_key = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = User
        fields = ('secret_key',)


