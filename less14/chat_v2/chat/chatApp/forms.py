from django.forms import forms, ModelForm, PasswordInput, CharField, TextInput

from chatApp.models import ChatUser
from chatApp.validators import not_null, email_validation


class RegistrationForm(ModelForm):
    class Meta:
        model = ChatUser

        fields = ["name", "login", "password"]
        widgets = {"password":PasswordInput()}

    def clean_login(self):
        user_name = self.cleaned_data["login"]
        email_validation(user_name)
        return self.cleaned_data["login"]
