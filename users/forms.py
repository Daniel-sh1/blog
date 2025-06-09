from django.contrib.auth.forms import ReadOnlyPasswordHashField, UsernameField
from django.utils.translation import gettext_lazy as _
from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class CustomUserForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        max_length=30,
        help_text="Используйте только российские EMAIL",
        widget=forms.TextInput(
            attrs={
                "type": "email",
                "class": "formatted-input"
            }
        )
    )
    class Meta:
        model = CustomUser
        fields = (
            "email",
            "username",
            "phone"
        )




class CustomUserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        label=_("Password"),
        help_text=_(
            "Raw passwords are not stored, so there is no way to see "
            "the user’s password."
        ),
    )

    class Meta:
        model = CustomUser
        fields = "__all__"
        field_classes = {"username": UsernameField}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        password = self.fields.get("password")
        if password:
            if self.instance and not self.instance.has_usable_password():
                password.help_text = _(
                    "Включите аутентификацию на основе пароля для этого пользователя, установив"
                    "пароль."
                )
        user_permissions = self.fields.get("user_permissions")
        if user_permissions:
            user_permissions.queryset = user_permissions.queryset.select_related(
                "content_type"
            )