from django import forms

from .models import Post, Category


# choices = [('coding', 'coding'), ('love', 'love')]
choices = Category.objects.all().values_list('name', 'name')

choice_list = []
for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'title_tag', 'snippets', 'author', 'category', 'body', 'images']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'snippets': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user', 'type': 'hidden'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control', 'placeholder': 'select'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'title_tag', 'snippets', 'category', 'body', 'images']

        widgets = {
            'title': forms.TimeInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TimeInput(attrs={'class': 'form-control'}),
            'snippets': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control', 'placeholder': 'select'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }