from django import forms
from user.models import User
from home.models import Work, Images
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegisterForm(UserCreationForm):
    _sys_users = ("admin", "administrator", "sys", "superuser")

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'id': 'full_name', 'placeholder': 'User name'},
        )
    )

    email = forms.EmailField(
        label='email',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'id': 'email', 'placeholder': 'Email'},
        )

    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'id': 'password', 'placeholder': 'Password'},
        )
    )

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'id': 'password_repeat', 'placeholder': 'Password repeat'},
    )
    )

    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'id': 'phone', 'placeholder': 'Phone'},
        )
    )

    class Meta:
        model = User
        fields = ("username", "phone", "email", "password1", 'password2')

    def clean(self):
        is_errors = False
        if self.cleaned_data.get('password') != self.cleaned_data.get('password_repeat'):
            is_errors = True
            self.add_error(
                "password", "Different values in fields 'password' and 'password repeat'."
            )
        if self.cleaned_data.get("username") in self._sys_users:
            is_errors = True
            self.add_error("username", "Invalid username.")
        if is_errors:
            raise forms.ValidationError("Invalid form.")
        return self.cleaned_data


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'id': 'full_name', 'placeholder': 'User name'},
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'id': 'password', 'placeholder': 'Password'},
        )
    )

    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']


class UpdateUserForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'id': 'full_name', 'placeholder': 'First Name'},
        )
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'id': 'full_name', 'placeholder': 'Last Name'},
        )
    )

    email = forms.EmailField(
        label='email',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'id': 'email', 'placeholder': 'Email'},
        )

    )

    avatar = forms.FileField(
        widget=forms.ClearableFileInput(
            attrs={'class': 'ask-signup-avatar-input', }),
        required=False,
    )

    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'id': 'phone', 'placeholder': 'Phone'},
        )
    )

    bio = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form_control w-100', 'id': 'bio', 'placeholder': '', 'rows': 4, },
        )
    )

    instagram = forms.URLField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'id': 'phone', 'placeholder': 'URL'},
        )
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'instagram', 'bio', 'phone', 'avatar']


class UserFormWorks(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'id': 'title', 'placeholder': 'Title'},
        )
    )

    text = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form_control w-100', 'id': 'Text', 'placeholder': 'Text', 'rows': 8, },
        )
    )

    email = forms.EmailField(
        label='email',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'id': 'email', 'placeholder': 'Email'},
        )

    )

    instagram = forms.URLField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'id': 'phone', 'placeholder': 'URL'},
        )
    )

    images = forms.FileField(
        label='Images',
        widget=forms.ClearableFileInput(
            attrs={'multiple': True, 'class': 'ask-signup-avatar-input', 'placeholder': 'images'}),
    )

    tags = forms.CharField(
        label='slug',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'id': 'email', 'placeholder': 'Tags'},
        )

    )

    class Meta:
        model = Work
        fields = ['title', 'text', 'email', 'instagram', 'images', 'tags']


class ImageForm(forms.Form):
    images = forms.FileField(
        label='Images',
        widget=forms.ClearableFileInput(
            attrs={'multiple': True, 'class': 'ask-signup-avatar-input', 'placeholder': 'images'}),
    )

    class Meta:
        model = Images
        fields = ('image',)
