from django import forms
from .models import Post, Category


class PostForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                      widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Post
        fields = ['category', 'title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }
