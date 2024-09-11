from django import forms
from registrodemanutencao.models import registrodemanutencao, ImagemRegistro
from cliente.models import Cliente
from produto.models import Produto
from .models import retorno
from django.conf import settings
import os
from django.utils import timezone

class FormulariosForm(forms.ModelForm):
    class Meta:
        model = registrodemanutencao
        fields = [
            'nome', 'tipo_produto', 'tipo_entrada', 'status', 'tipo_customizacao', 
            'recebimento', 'id_equipamentos', 'entregue_por_retirado_por', 'data_criacao', 'customizacaoo'
        ]
        widgets = {
            'nome': forms.Select(attrs={'class': 'form-control'}),
            'tipo_produto': forms.Select(attrs={'class': 'form-control'}),
            'customizacaoo': forms.Select(attrs={'class': 'form-control'}),
            'tipo_entrada': forms.Select(attrs={'class': 'form-control'}),
            'tipo_customizacao': forms.Select(attrs={'class': 'form-control'}),
            'recebimento': forms.Select(attrs={'class': 'form-control'}),
            'entregue_por_retirado_por': forms.Select(attrs={'class': 'form-control'}),
            'id_equipamentos': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'data_criacao': forms.TextInput(attrs={'class': 'form-control'}),
        }

class FormulariosUpdateForm(forms.ModelForm):
    class Meta:
        model = registrodemanutencao
        fields = [
            'nome', 'tipo_produto', 'motivo', 'faturamento', 'tipo_entrada', 'tratativa', 
            'status', 'tipo_customizacao', 'entregue_por_retirado_por', 'setor', 'customizacaoo', 'id_equipamentos'
        ]
        widgets = {
            'nome': forms.Select(attrs={'class': 'form-control'}),
            'tipo_produto': forms.Select(attrs={'class': 'form-control'}),
            'motivo': forms.Select(attrs={'class': 'form-control'}),
            'tipo_entrada': forms.Select(attrs={'class': 'form-control'}),
            'tipo_customizacao': forms.Select(attrs={'class': 'form-control'}),
            'entregue_por_retirado_por': forms.TextInput(attrs={'class': 'form-control'}),
            'faturamento': forms.Select(attrs={'class': 'form-control'}),
            'customizacaoo': forms.Select(attrs={'class': 'form-control'}),
            'id_equipamentos': forms.TextInput(attrs={'class': 'form-control'}),
            'tratativa': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'setor': forms.Select(attrs={'class': 'form-control'}),
        }

from django.forms import inlineformset_factory

ImagemRegistroFormSet = inlineformset_factory(
    registrodemanutencao,
    ImagemRegistro,
    fields=('imagem', 'descricao', 'setorid', 'tipo_problema'),
    extra=1,
    can_delete=True,
    widgets={
        'imagem': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        'setorid': forms.Select(attrs={'class': 'form-control'}),
        'tipo_problema': forms.Select(attrs={'class': 'form-control'}),
    }
)

class RetornoForm(forms.ModelForm):
    class Meta:
        model = retorno
        fields = [
            'cliente', 'produto', 'tipo_problema', 'imagem', 'id_equipamentos'
        ]
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'id_equipamentos': forms.TextInput(attrs={'class': 'form-control'}),
            'produto': forms.Select(attrs={'class': 'form-control'}),
            'tipo_problema': forms.Select(attrs={'class': 'form-control'}),
            'imagem': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
