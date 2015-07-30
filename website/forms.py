from django import forms

from website.models import OneWord

class OneWordForm(forms.ModelForm):
    class Meta:
        model = OneWord
        fields = ['word', 'footer', 'fg_color', 'bg_color']
        widgets = {
                        'word': forms.TextInput(attrs={'placeholder': "Word you want to scream"}),
                        'footer': forms.TextInput(attrs={'placeholder': "Additional text"}),
            }
        labels = {
                        'footer': "More words",
                        'fg_color': "Text color",
                        'bg_color': "Background color",
            }
