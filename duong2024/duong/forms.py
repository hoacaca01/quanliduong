from django import forms
from .models import Street

class StreetForm(forms.ModelForm):
    class Meta:
        model = Street
        fields = ['stt', 'name', 'category', 'category2', 'description', 'importance_level', 'significance', 'longitude', 'latitude']
        widgets = {
            'stt': forms.NumberInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'category2': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'importance_level': forms.TextInput(attrs={'class': 'form-control'}),
            'significance': forms.TextInput(attrs={'class': 'form-control'}),
            'longitude': forms.TextInput(attrs={'class': 'form-control'}),
            'latitude': forms.TextInput(attrs={'class': 'form-control'}),
        }
class UploadFileForm(forms.Form):
    file = forms.FileField()