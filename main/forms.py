from datetime import date
from django import forms

class URLForm(forms.Form):

    url = forms.CharField(
        max_length=250,
        label = "Paste your tab's URL below",
        # initial='https://tabs.ultimate-guitar.com/tab/rick_astley/never_gonna_give_you_up_tabs_1970139',
        widget=forms.TextInput(attrs={'placeholder': 'Enter Ultimate-Guitar URL', 'class': 'shadow-sm p-3 mb-5 bg-white rounded'})
    )


