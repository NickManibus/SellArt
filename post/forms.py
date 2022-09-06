from post.models import Comment
from django import forms
from django.core.exceptions import ValidationError


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', 'email', 'name')

        widgets = {'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name', 'placeholder': 'Name'}),
                   'email': forms.TextInput(attrs={'class': 'form-control', 'id': 'email', 'placeholder': 'Email'}),
                   'text': forms.Textarea(attrs={'class': 'form_control w-100', 'id': 'text', 'placeholder': 'Comment',
                                                 'rows': 5, }),
                   }

    # def __init__(self, *args, **kwargs):
    #     """Save the request with the form so it can be accessed in clean_*()"""
    #     self.request = kwargs.pop('request', None)
    #     super(CommentForm, self).__init__(*args, **kwargs)

    def clean_name(self):
        data =self.cleaned_data['name']
        if not self.request.user.is_authenticated and data.lower().strip() == 'admin':
            raise ValidationError('Sorry, you cannot use this name.')
        return data