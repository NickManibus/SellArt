from home.models import FeedBackContact
from django.forms import ModelForm
from django import forms


class FormContact(forms.ModelForm):
    class Meta:

        model = FeedBackContact
        fields = ['full_name', 'email', 'message']

    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'id': 'full_name', 'placeholder': 'Full name'},
        )
    )

    email = forms.EmailField(
        label='email',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'id': 'email', 'placeholder': 'Email'},
        )

    )

    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form_control w-100', 'id': 'message', 'placeholder': 'Message', 'rows': 5, },
        )
    )

    def clean(self):
        if self.cleaned_data.get('full_name') == 'full_name':
            self.add_error('full_name', 'Вы уже отправили сообщение')
            self.add_error('full_name', 'не корректный символ')
            self.add_error('email', 'не корректный символ')
            raise forms.ValidationError('Попробуйте еще раз')
        return self.cleaned_data

    # def save(self, **kwargs):
    #     adminmodel = FeedBackContact(**self.cleaned_data)
    #     adminmodel.save()
