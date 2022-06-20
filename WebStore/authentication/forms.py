from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, UserCreationForm
from .models import Account
from django.forms import HiddenInput


class LoginForm(AuthenticationForm):
    class Meta:
        model = Account
        fields = (
            "username",
            "password"
        )

    def __init__(self, *arg, **kwarg):
        super(LoginForm, self).__init__(*arg, **kwarg)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


class EditAccountForm(UserChangeForm):
    class Meta:
        model = Account
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "age",
            "gender",
            "address",
            "image",
        )

    def __init__(self, *arg, **kwarg):
        super(EditAccountForm, self).__init__(*arg, **kwarg)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            if field_name == "password":
                field.widget = HiddenInput()


class RegistrationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = (
            "username",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "email",
            "age",
            "gender",
            "address",
            "image"
        )

    def __init__(self, *arg, **kwarg):
        super(RegistrationForm, self).__init__(*arg, **kwarg)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            if field_name == "password":
                field.widget = HiddenInput()
