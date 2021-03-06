from django import forms

from website.models import OneWord

class OneWordForm(forms.ModelForm):
    class Meta:
        model = OneWord
        fields = ['word', 'footer', 'fg_color', 'bg_color']
        widgets = {
                        'word': forms.TextInput(attrs={'placeholder': ""}),
                        'footer': forms.TextInput(attrs={'placeholder': ""}),
                        'fg_color': forms.TextInput(attrs={'class': 'color'}),
                        'bg_color': forms.TextInput(attrs={'class': 'color'}),
            }
        labels = {
                        'footer': "More words",
                        'fg_color': "Text color",
                        'bg_color': "Background color",
            }
