from django import forms
from .models import GonderiModel

class GonderiForm(forms.ModelForm):
    class Meta:
        model=GonderiModel
        fields = ('baslik','yazi','tur')