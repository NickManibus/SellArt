from django import forms
from user.models import User
from home.models import Work, Tags
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.core import validators


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

    def init(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'request' in kwargs:
            self.request = kwargs.pop('request')
        super(RegForm, self).__init__(*args, **kwargs)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Имя пользователя уже существуе")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Почтовый ящик уже существует")
        return email


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

    avatar = forms.ImageField(
        widget=forms.FileInput(
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

        def clean_avatar(self):
            avatar = self.cleaned_data.get('avatar')
            if avatar is None:
                raise forms.ValidationError(u'Добавьте картинку')
            if 'image' not in avatar.content_type:
                raise forms.ValidationError(u'Неверный формат картинки')
            return avatar


class UserFormWorks(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Tags.objects.all())


    class Meta:
        model = Work
        fields = ['title', 'text', 'email', 'instagram', 'image', 'image1', 'image2', 'tags', ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'title', 'placeholder': 'Title'}),
            'text': forms.Textarea(
                attrs={'class': 'form_control w-100', 'id': 'Text', 'placeholder': 'Text', 'rows': 8, }),
            'email': forms.TextInput(attrs={'class': 'form-control', 'id': 'email', 'placeholder': 'Email'}),
            'instagram': forms.TextInput(attrs={'class': 'form-control', 'id': 'phone', 'placeholder': 'URL'}),
            'image': forms.ClearableFileInput(attrs={'class': 'input', 'placeholder': 'images'}),
            'image1': forms.ClearableFileInput(attrs={'class': 'input', 'placeholder': 'images'}),
            'image2': forms.ClearableFileInput(attrs={'class': 'input', 'placeholder': 'images'})

        }


    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Slig may not be "Create" ')
        if Work.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Slug must be unique. We have "{}" slug already'.format(new_slug))
        return new_slug

    def clean(self):
        if self.cleaned_data.get('title') == 'title':
            self.add_error('title', 'There is already a header with the same name')
            self.add_error('title', 'invalid character ')
            self.add_error('email', 'invalid character Email')
            self.add_error('tags', 'Select tags')
            raise forms.ValidationError('Try again')
        return self.cleaned_data
