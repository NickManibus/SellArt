from post.models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', 'email', 'name')

        widgets = {'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name', 'placeholder': 'Name'}),
                   'email': forms.TextInput(attrs={'class': 'form-control', 'id': 'email', 'placeholder': 'Email'}),
                   'text': forms.Textarea(attrs={'class': 'form_control w-100', 'id': 'text', 'placeholder': 'Comment',
                                                 'rows': 5, }),
                   }
