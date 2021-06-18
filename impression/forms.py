from .models import Impression
from django.forms import ModelForm


class ImpressionForm(ModelForm):
    class Meta:
        model = Impression
        fields = ['name_impression', 'comment_impression', 'location']
        

