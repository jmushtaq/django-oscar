from django import forms
from .models import Theme

class ThemeSelectionForm(forms.Form):
    theme = forms.ModelChoiceField(
        queryset=Theme.objects.all(),
        widget=forms.RadioSelect,
        empty_label=None
    )
