from typing import Any
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from registrodemanutencao.models import registrodemanutencao
from requisicao.models import Requisicoes
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.conf import settings
from registrodemanutencao.forms import FormulariosUpdateForm
from django.core.mail import send_mail
from django.contrib.auth.mixins import PermissionRequiredMixin,LoginRequiredMixin
#------------------------------------------------------
class RequisicoesViews(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = Requisicoes
    template_name = "requisicoes.html"
    context_object_name = 'requisicoes'
    paginate_by = 10
    permission_required = "requisicao.view_requisicoes"
    
    def get_queryset(self):
        return Requisicoes.objects.filter(status__in=['Pendente'])
    


from django.http import JsonResponse
from .models import Clientes


def get_cliente_data(request, cliente_id):
    cliente = Clientes.objects.get(id=cliente_id)
    data = {
        'cnpj': cliente.cnpj,
        'inicio_de_contrato': cliente.inicio_de_contrato,
        'vigencia': cliente.vigencia,
        'contrato': cliente.tipo_contrato,
        'endereco': cliente.endereco,
    }
    return JsonResponse(data) 
    
class requisicoescrateview(PermissionRequiredMixin,LoginRequiredMixin,CreateView):
    model = models.Requisicoes
    template_name = 'requisicao_create.html'
    form_class = forms.requisicaoForm
    success_url = reverse_lazy('requisicoes')
    permission_required="requisicao.add_requisicoes"


class RequisicaoDetailView(PermissionRequiredMixin,LoginRequiredMixin,DetailView):
    model = models.Requisicoes
    template_name = 'requisicao_detail.html'
    permission_required="requisicao.view_requisicoes"


class RequisicaoUpdateView(PermissionRequiredMixin,LoginRequiredMixin,UpdateView):
    model = Requisicoes
    form_class = forms.requisicaoForm
    template_name = 'requisicao_update.html'
    context_object_name = 'requisicao'
    success_url = reverse_lazy('requisicao_list')
    permission_required="requisicao.change_requisicoes"

  

class requisicoesdeleteview(PermissionRequiredMixin,LoginRequiredMixin,DeleteView):
    model = models.Requisicoes
    template_name = 'requisicao_delete.html'
    success_url = reverse_lazy('acompanhamento_requisicao')
    permission_required="requisicao.delete_requisicoes"
#------------------------------------------------------

#------------------------------------------------------
class configuracaodeleteview(PermissionRequiredMixin,LoginRequiredMixin,DeleteView):
    model = models.Requisicoes
    template_name = 'configuracao_delete.html'
    success_url = reverse_lazy('acompanhamento_requisicao')
    permission_required="requisicao.delete_requisicoes"


class ConfiguracaoListView(PermissionRequiredMixin,LoginRequiredMixin,ListView):
    template_name = 'configuracao_list.html'
    context_object_name = 'equipamentos'
    permission_required= "requisicao.view_requisicoes"
    
    
    def get_queryset(self):
        requisicoes_queryset = Requisicoes.objects.filter(status__in=['Aprovado pelo CEO'])
        manutencao_queryset = registrodemanutencao.objects.filter(status__in=['Aprovado Inteligência', 'Aprovado pela Diretoria', 'Aprovado pelo CEO'])
        
        # Combine os querysets
        combined_queryset = list(requisicoes_queryset) + list(manutencao_queryset)
        
        return combined_queryset


class ConfiguracaoUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Requisicoes
    form_class = forms.requisicaoForm
    template_name = 'configuracao_update.html'
    context_object_name = 'equipamento'
    success_url = reverse_lazy('ConfiguracaoListView')
    permission_required = "requisicao.change_requisicoes"

class ConfiguracaoUpdateView2(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = registrodemanutencao
    form_class = FormulariosUpdateForm
    template_name = 'configuracao_update.html'
    context_object_name = 'equipamento'
    success_url = reverse_lazy('ConfiguracaoListView')
    permission_required = "requisicao.change_requisicoes"
  

 #------------------------------------------------------   

   
#------------------------------------------------------
class ceoListViews(PermissionRequiredMixin,LoginRequiredMixin,ListView):
    model = Requisicoes
    template_name = "ceo_list.html"
    context_object_name = 'ceo_list'
    paginate_by = 10
    permission_required="requisicao.view_requisicoes"
    def get_queryset(self):
        return Requisicoes.objects.filter(status__in=['Pendente','Aprovado pela Diretoria'])
  

class ceodetailview(PermissionRequiredMixin,LoginRequiredMixin,DetailView):
    model = Requisicoes
    template_name = 'ceo_detail.html'
    permission_required="requisicao.view_requisicoes"


class CeoEntradaDetailView(PermissionRequiredMixin,LoginRequiredMixin,DetailView):
    model = registrodemanutencao
    template_name = 'ceo_detalheentrada.html'
    context_object_name = 'manutencoes'
    permission_required="requisicao.view_requisicoes"
#------------------------------------------------------


#------------------------------------------------------


class diretoriaListViews(PermissionRequiredMixin,LoginRequiredMixin,ListView):
    template_name = "diretoria_list.html"
    context_object_name = 'diretoria_list'
    permission_required="requisicao.view_requisicoes"
    
    def get_queryset(self):
        requisicoes_queryset = Requisicoes.objects.filter(status__in=['', ''])
        manutencao_queryset = registrodemanutencao.objects.filter(status='Manutenção')
        
        # Combine os querysets
        combined_queryset = list(requisicoes_queryset) + list(manutencao_queryset)
        
        return combined_queryset
#------------------------------------------------------

#------------------------------------------------------
class expedicaoListViews(PermissionRequiredMixin,LoginRequiredMixin,ListView):
    model = Requisicoes
    template_name = "expedicao_list.html"
    context_object_name = 'expedicao_list'
    permission_required="requisicao.view_requisicoes"
    
       
    def get_queryset(self):
        requisicoes_queryset = Requisicoes.objects.filter(status__in=['Configurado'])
        manutencao_queryset = registrodemanutencao.objects.filter(status__in=['Configurado'])
        
        # Combine os querysets
        combined_queryset = list(requisicoes_queryset) + list(manutencao_queryset)
        
        return combined_queryset
#------------------------------------------------------
#------------------------------------------------------
class historicoListView(PermissionRequiredMixin,LoginRequiredMixin,ListView):
    model = Requisicoes
    template_name = "historico_list.html"
    context_object_name = 'historico_list'
    paginate_by = 10 
    permission_required="requisicao.view_requisicoes"
    
    def get_queryset(self):
        queryset = Requisicoes.objects.filter(status__in=['Enviado para o Cliente', 'Reprovado pelo CEO'])
        nome = self.request.GET.get('nome')
        id_equipamentos = self.request.GET.get('id_equipamentos')
        
        if nome:
            queryset = queryset.filter(nome__nome__icontains=nome)
        
        if id_equipamentos:
            queryset = queryset.filter(id_equipamentos__icontains=id_equipamentos)
        
        return queryset

#------------------------------------------------------





#------------------------------------------------------
def aprovar_requisicao(request, id):
    registro = get_object_or_404(Requisicoes, id=id)
    registro.status = 'Aprovado pela Diretoria'
    registro.save()
    return redirect('#')

def reprovar_requisicao(request, id):
    registro = get_object_or_404(Requisicoes, id=id)
    registro.status = 'Reprovado pela Diretoria'
    registro.save()
    return redirect('#')
#------------------------------------------------------

#------------------------------------------------------
def reprovar_ceo(request, id):
    registro = get_object_or_404(Requisicoes, id=id)
    registro.status = 'Reprovado pelo CEO'
    registro.save()
    
    return redirect('ceoListViews')


def aprovar_ceo(request, id):
    registro = get_object_or_404(Requisicoes, id=id)
    registro.status = 'Aprovado pelo CEO'
    registro.save()
    subject = f"Requisicao Aprovada: {registro.id}"
    message = f"A manutenção {registro.id} foi aprovada com sucesso. {registro.nome} Status: {registro.status} criar Requisição"
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = ['sjuniorr6@gmail.com']
    
    try:
        send_mail(subject, message, from_email, recipient_list)
        print("Email enviado com sucesso.")
    except Exception as e:
        print(f"Erro ao enviar email: {e}")
    
    

    return redirect('ceoListViews')
    
    
#------------------------------------------------------


#------------------------------------------------------
from django.http import HttpResponse
def configurado_expedicao(request, id):
    registro = get_object_or_404(Requisicoes, id=id)
    registro.status = 'Configurado'
    registro.save()
    return redirect('ConfiguracaoListView')

def expedicao_expedido(request, id):
    registro = get_object_or_404(Requisicoes, id=id)
    registro.status = 'Enviado para o Cliente'
    registro.save()
    return redirect('expedicaoListViews')

def expedicao_expedido2(request, id):
    registro = get_object_or_404(registrodemanutencao, id=id)
    registro.status = 'Enviado para o Cliente'
    registro.save()
    return redirect('expedicaoListViews')


def expedir_requisicao(request, id):
    registro = get_object_or_404(Requisicoes, id=id)
    # Alterar o status do registro para "Configurado"
    registro.status = 'Configurado'
    registro.save()
    return redirect('ConfiguracaoListView')

def expedir_manutencao(request, id):
    registro = get_object_or_404(registrodemanutencao, id=id)
    # Alterar o status do registro para "Configurado"
    registro.status = 'Configurado'
    registro.save()
    return redirect('ConfiguracaoListView')






def configurado_manutencao(request, id):
    registro = get_object_or_404(registrodemanutencao, id=id)
    registro.status = 'Configurado'
    registro.save()
    return redirect('ConfiguracaoListView')


def expedicao_expedido_manutencao(request, id):
    registro = get_object_or_404(registrodemanutencao, id=id)
    registro.status = 'Enviado para o Cliente'
    registro.save()
    return redirect('expedicaoListViews')


#------------------------------------------------------
# View para aprovar uma requisição pela diretoria
#------------------------------------------------------
def Reprovar_diretoria(request, id):
    registro = get_object_or_404(registrodemanutencao, id=id)
    registro.status = 'Reprovado pela Diretoria'
    registro.save()
    return redirect('diretoriaListViews')
   

# View para reprovar uma requisição pela diretoria
def Aprovar_diretoria(request, id):
    registro = get_object_or_404(registrodemanutencao, id=id)
    registro.status = 'Aprovado pela Diretoria'  # Corrigido para "Aprovado pela Diretoria"
    registro.save()

    subject = f"Manutenção Aprovada: {registro.id}"
    message = f"A manutenção {registro.id} foi aprovada com sucesso. {registro.nome} Status: {registro.status} criar Requisição"
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = ['sjuniorr6@gmail.com']
    
    try:
        send_mail(subject, message, from_email, recipient_list)
        print("Email enviado com sucesso.")
    except Exception as e:
        print(f"Erro ao enviar email: {e}")
    
    

    return redirect('diretoriaListViews')


#------------------------------------------------------
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Paragraph, SimpleDocTemplate
from reportlab.lib.styles import ParagraphStyle
from django.conf import settings
import os
import datetime

def gerar_pdf_requisicao(requisicao):
    pdf_path = os.path.join(settings.MEDIA_ROOT, f'requisicao-{requisicao.id}.pdf')
    p = canvas.Canvas(pdf_path, pagesize=letter)
    p.setTitle(f'Requisição - {requisicao.id}')

    # Cabeçalho
    p.setFont("Helvetica-Bold", 16)
    p.setFillColor(colors.HexColor("#004B87"))
    y_position = 750
    p.drawString(100, y_position, "Relatório de Requisição")
    y_position -= 30

    # Adicionar imagens de cabeçalho
    imagem_padrao = os.path.join(settings.MEDIA_ROOT, 'imagens_registros/SIDNEISIDNEISIDNEI.png')
    imagem_qrcode = os.path.join(settings.MEDIA_ROOT, 'imagens_registros/qrcode.png')
    image_width, image_height = 200, 100
    page_width, page_height = letter
    total_width = image_width * 2 + 20
    x_position = (page_width - total_width) / 2

    p.setFillColor(colors.white)
    p.rect(x_position - 10, y_position - image_height - 10, total_width + 20, image_height + 20, fill=1)
    p.drawImage(imagem_padrao, x_position, y_position - image_height, width=image_width, height=image_height)
    p.drawImage(imagem_qrcode, x_position + image_width + 20, y_position - image_height, width=image_width, height=image_height)
    y_position -= (image_height + 20)

    p.setFont("Helvetica", 12)
    p.setFillColor(colors.black)


    def draw_text(p, theme, value, x, y, max_width):
        theme_style = ParagraphStyle('ThemeStyle', fontName='Helvetica-Bold', fontSize=12)
        value_style = ParagraphStyle('ValueStyle', fontName='Helvetica', fontSize=12)
        
        theme_paragraph = Paragraph(f"<b>{theme}</b>", theme_style)
        value_paragraph = Paragraph(value, value_style)
        
        theme_width, theme_height = theme_paragraph.wrap(max_width, y)
        value_width, value_height = value_paragraph.wrap(max_width, y)
        
        theme_paragraph.drawOn(p, x, y - theme_height)
        y -= theme_height
        value_paragraph.drawOn(p, x, y - value_height)
        y -= value_height + 10  # Espaçamento entre linhas
        
        return y

    def check_space(p, y_position, required_space):
        if y_position - required_space < 50:
            p.showPage()
            p.setFont("Helvetica", 12)
            p.setFillColor(colors.black)
            return 750
        return y_position

    def draw_text(p, theme, value, x, y, max_width):
        theme_style = ParagraphStyle('ThemeStyle', fontName='Helvetica-Bold', fontSize=12)
        value_style = ParagraphStyle('ValueStyle', fontName='Helvetica', fontSize=12)
        
        theme_paragraph = Paragraph(f"<b>{theme}</b>", theme_style)
        value_paragraph = Paragraph(value, value_style)
        
        theme_width, theme_height = theme_paragraph.wrap(max_width, y)
        value_width, value_height = value_paragraph.wrap(max_width, y)
        
        theme_paragraph.drawOn(p, x, y - theme_height)
        y -= theme_height
        value_paragraph.drawOn(p, x, y - value_height)
        y -= value_height + 10  # Espaçamento entre linhas
        
        return y

    def check_space(p, y_position, required_space):
        if y_position - required_space < 50:
            p.showPage()
            p.setFont("Helvetica", 12)
            p.setFillColor(colors.black)
            return 750
        return y_position

    def safe_draw_text(p, theme, value, x, y, max_width):
        if isinstance(value, str):
            return draw_text(p, theme, value, x, y, max_width)
        else:
            return draw_text(p, theme, str(value), x, y, max_width)

    def add_text_with_check(p, theme, value, x, y, max_width):
        required_space = 50  # Espaço necessário para cada entrada de texto
        y = check_space(p, y, required_space)
        return safe_draw_text(p, theme, value, x, y, max_width)

    y_position = add_text_with_check(p, "Registro #:", requisicao.id, 100, y_position, 400)
    y_position = add_text_with_check(p, "Nome:", requisicao.nome, 100, y_position, 400)
    y_position = add_text_with_check(p, "Status:", requisicao.status, 100, y_position, 400)
    y_position = add_text_with_check(p, "Endereço:", requisicao.endereco, 100, y_position, 400)
    y_position = add_text_with_check(p, "Contrato:", requisicao.contrato, 100, y_position, 400)
    y_position = add_text_with_check(p, "CNPJ:", requisicao.cnpj, 100, y_position, 400)
    
    # Verificar se os campos são objetos de data antes de chamar strftime
    if isinstance(requisicao.inicio_de_contrato, (datetime.date, datetime.datetime)):
        y_position = add_text_with_check(p, "Início do Contrato:", requisicao.inicio_de_contrato.strftime("%d/%m/%Y"), 100, y_position, 400)
    else:
        y_position = add_text_with_check(p, "Início do Contrato:", requisicao.inicio_de_contrato, 100, y_position, 400)
    
    if isinstance(requisicao.vigencia, (datetime.date, datetime.datetime)):
        y_position = add_text_with_check(p, "Vigência:", requisicao.vigencia.strftime("%d/%m/%Y"), 100, y_position, 400)
    else:
        y_position = add_text_with_check(p, "Vigência:", requisicao.vigencia, 100, y_position, 400)
    
    if isinstance(requisicao.data, (datetime.date, datetime.datetime)):
        y_position = add_text_with_check(p, "Data:", requisicao.data.strftime("%d/%m/%Y"), 100, y_position, 400)
    else:
        y_position = add_text_with_check(p, "Data:", requisicao.data, 100, y_position, 400)
    
    y_position = add_text_with_check(p, "Motivo:", requisicao.motivo, 100, y_position, 400)
    y_position = add_text_with_check(p, "Envio:", requisicao.envio, 100, y_position, 400)
    y_position = add_text_with_check(p, "Taxa de Envio:", requisicao.taxa_envio, 100, y_position, 400)
    y_position = add_text_with_check(p, "Comercial:", requisicao.comercial, 100, y_position, 400)
    y_position = add_text_with_check(p, "Tipo de Produto:", requisicao.tipo_produto, 100, y_position, 400)
    y_position = add_text_with_check(p, "Carregador:", requisicao.carregador, 100, y_position, 400)
    y_position = add_text_with_check(p, "Cabo:", requisicao.cabo, 100, y_position, 400)
    y_position = add_text_with_check(p, "Tipo de Fatura:", requisicao.tipo_fatura, 100, y_position, 400)
    y_position = add_text_with_check(p, "Valor Unitário:", requisicao.valor_unitario, 100, y_position, 400)
    y_position = add_text_with_check(p, "Valor Total:", requisicao.valor_total, 100, y_position, 400)
    y_position = add_text_with_check(p, "Formas de Pagamento:", requisicao.forma_pagamento, 100, y_position, 400)
    y_position = add_text_with_check(p, "Observações:", requisicao.observacoes, 100, y_position, 400)
    y_position = add_text_with_check(p, "TP:", requisicao.TP, 100, y_position, 400)
    y_position = add_text_with_check(p, "ID Equipamentos:", requisicao.id_equipamentos, 100, y_position, 400)

    # Feche o objeto PDF e salve no caminho especificado.
    p.showPage()
    p.save()

    return pdf_path
from django.core.mail import EmailMessage
from django.shortcuts import get_object_or_404, redirect
from django.conf import settings
from .models import Requisicoes

def enviar_email_com_pdf(request, id):
    requisicao = get_object_or_404(Requisicoes, id=id)
    pdf_path = gerar_pdf_requisicao(requisicao)
    
    subject = f"Requisição Criada: {requisicao.id}"
    message = f"A requisição {requisicao.id} foi criada com sucesso. Segue PDF para tratativa."
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = ['sjuniorr6@gmail.com']
    
    email = EmailMessage(subject, message, from_email, recipient_list)
    email.attach_file(pdf_path)
    
    try:
        email.send()
        print("Email enviado com sucesso.")
    except Exception as e:
        print(f"Erro ao enviar email: {e}")
    
    return redirect('requisicoesListView')

from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Requisicoes

def download_pdf_requisicao(request, id):
    requisicao = get_object_or_404(Requisicoes, id=id)
    pdf_path = gerar_pdf_requisicao(requisicao)
    
    with open(pdf_path, 'rb') as pdf_file:
        response = HttpResponse(pdf_file.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="requisicao-{requisicao.id}.pdf"'
        return response