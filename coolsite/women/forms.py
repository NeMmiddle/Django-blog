from django import forms
from .models import *


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, label='Заголовок')
    slug = forms.SlugField(max_length=255, label='URL')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 10}), label='Контент')
    is_published = forms.BooleanField(label='Публикация')
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категория")
