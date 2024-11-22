from django import forms

class ContactForms(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='Name',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Nome do contato'}
        )
    )
    email = forms.EmailField(
        max_length=100,
        label='Email',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Email para contato'}
        )
    )
    telefone = forms.CharField(
        max_length=20,
        label='Telefone',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Ex: +__(__)________'}
        )
    )
    empresa = forms.CharField(
        max_length=100,
        label='Empresa',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Nome da empresa'}
        )
    )
    numero_de_funcionarios = forms.ChoiceField(
        choices=[
            ('1', '1 - 10 funcionários'),
            ('2', '10 - 50 funcionários'),
            ('3', '+50 funcionários')
        ],
        widget=forms.RadioSelect,
        label='Número de Funcionários'
    )
    mensagem = forms.CharField(
        label='Mensagem',
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'placeholder': 'Digite a mensagem'}
        )
    )
