from datetime import date


class URLForm(forms.Form):

    url = forms.CharField(
        label='URL',
        max_length=250,
        initial='https://tabs.ultimate-guitar.com/tab/rick_astley/never_gonna_give_you_up_tabs_1970139'
        help_text='Paste the URL of your tab'
    )

