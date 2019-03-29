from datetime import date
from django import forms

class URLForm(forms.Form):

    url = forms.CharField(
        # label='URL',
        max_length=250,
        # initial='https://tabs.ultimate-guitar.com/tab/rick_astley/never_gonna_give_you_up_tabs_1970139',
        help_text='Paste the URL of your tab',
        widget=forms.TextInput(attrs={'placeholder': 'Enter Ultimate-Tabs URL', 'class': 'shadow-sm p-3 mb-5 bg-white rounded'})
    )


