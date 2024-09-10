from django import forms
from .models import regcliente


class regclientes(forms.ModelForm):
    class Meta:
        model = regcliente  # Especifique o modelo aqui
        fields = ['nome', 'franquia_km', 'franquiah', 'valor_acionamento', 'valorkm','valor_exedente']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'franquia_km': forms.TextInput(attrs={'class': 'form-control'}), 
            'franquiah' : forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'valor_acionamento': forms.NumberInput(attrs={'class': 'form-control'}),
            'valorkm': forms.NumberInput(attrs={'class': 'form-control'}),
            'valor_exedente': forms.NumberInput(attrs={'class': 'form-control'}),
        }