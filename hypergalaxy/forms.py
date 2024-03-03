from django import forms

class FormContato(forms.Form):
    nome = forms.CharField(max_length=120, widget=forms.TextInput(attrs={
        'class':'input w-input',
        'placeholder':'Ex. David',
        'id':'Nome'
    }))

    servico = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        "style":"display:none;",
        "id":"servicos"
    }))

    email = forms.EmailField(max_length=120, widget=forms.EmailInput(attrs={
        'class':'input w-input',
        'placeholder':'Ex. David@gmail.com',
        'id':'email'
    }))

    assunto = forms.CharField(max_length=120, widget=forms.Textarea(attrs={
        'class':'input w-input',
        'placeholder':'Ex. Conte-nos mais sobre sua ideia',
        'id':'Message'
    }))