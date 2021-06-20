from .models import Impression
from django import forms


class ImpressionForm(forms.ModelForm):
    class Meta:
        model = Impression
        fields = ['name_impression', 'comment_impression', 'location']
        
        widgets = {
            'name_impression': forms.TextInput(attrs={'class': 'form-contronl'}),
            'comment_impression': forms.Textarea(attrs={'class': 'form-contronl'}),
            'location': forms.TextInput(attrs={'class': 'form-contronl'}),

        }

