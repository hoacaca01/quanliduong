# from django import forms
# from .models import Street
#
# class StreetForm(forms.ModelForm):
#     class Meta:
#         model = Street
#         fields = '__all__'
#         widgets = {
#             'stt': forms.NumberInput(attrs={'required': False}),
#             'category': forms.TextInput(attrs={'required': False}),
#             'description': forms.Textarea(attrs={'required': False}),
#             'importance_level': forms.TextInput(attrs={'required': False}),
#             'significance': forms.TextInput(attrs={'required': False}),
#         }

from django import forms
from .models import Street

class StreetForm(forms.ModelForm):
    class Meta:
        model = Street
        fields = ['stt', 'name', 'category', 'description', 'importance_level', 'significance', 'longitude', 'latitude']
        widgets = {
            'stt': forms.NumberInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'importance_level': forms.TextInput(attrs={'class': 'form-control'}),
            'significance': forms.TextInput(attrs={'class': 'form-control'}),
            'longitude': forms.TextInput(attrs={'class': 'form-control'}),
            'latitude': forms.TextInput(attrs={'class': 'form-control'}),
        }
