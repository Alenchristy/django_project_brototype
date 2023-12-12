from django.forms import ModelForm
from django import forms
from .models import MovieInfo

class MovieForm(ModelForm):
    class Meta:
        model = MovieInfo
        fields = '__all__'
        

    # widgets = {
    #     'title': forms.TextInput(attrs={'style': 'color: blue; font-weight: bold;'}),
    #     'year': forms.NumberInput(attrs={'style': 'color: red; font-weight: bold;'}),
    #     'description': Textarea(attrs={'style': 'color: green; text-align: center;'}),
    # }
