from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.urls import reverse_lazy

from .models import (
    Paciente,
    Profissional,
    Especialidade,
    Agenda,
    Consulta,
    Prontuario,
    Pagamento
)


# =====================================================
# PACIENTE
# =====================================================

class PacienteCreate(CreateView):
    model = Paciente
    fields = ['usuario', 'cpf', 'telefone', 'data_nascimento', 'endereco']
    template_name = 'website/form.html'
    success_url = reverse_lazy('paciente-list')

    extra_context = {
        'titulo': 'Cadastro de Paciente',
        'botao': 'Cadastrar Paciente'
    }


class PacienteUpdate(UpdateView):
    model = Paciente
    fields = ['usuario', 'cpf', 'telefone', 'data_nascimento', 'endereco']
    template_name = 'website/form.html'
    success_url = reverse_lazy('paciente-list')

    extra_context = {
        'titulo': 'Editar Paciente',
        'botao': 'Salvar Alterações'
    }


class PacienteDelete(DeleteView):
    model = Paciente
    template_name = 'website/form.html'
    success_url = reverse_lazy('paciente-list')

    extra_context = {
        'titulo': 'Excluir Paciente',
        'botao': 'Confirmar Exclusão'
    }


class PacienteList(ListView):
    model = Paciente
    template_name = 'website/list/paciente.html'
    paginate_by = 10


class PacienteDetail(DetailView):
    model = Paciente
    template_name = 'website/detail/paciente.html'


# =====================================================
# ESPECIALIDADE
# =====================================================

class EspecialidadeCreate(CreateView):
    model = Especialidade
    fields = ['nome', 'descricao']
    template_name = 'website/form.html'
    success_url = reverse_lazy('especialidade-list')

    extra_context = {
        'titulo': 'Cadastro de Especialidade',
        'botao': 'Cadastrar Especialidade'
    }


class EspecialidadeUpdate(UpdateView):
    model = Especialidade
    fields = ['nome', 'descricao']
    template_name = 'website/form.html'
    success_url = reverse_lazy('especialidade-list')

    extra_context = {
        'titulo': 'Editar Especialidade',
        'botao': 'Salvar Alterações'
    }


class EspecialidadeDelete(DeleteView):
    model = Especialidade
    template_name = 'website/form.html'
    success_url = reverse_lazy('especialidade-list')

    extra_context = {
        'titulo': 'Excluir Especialidade',
        'botao': 'Confirmar Exclusão'
    }


class EspecialidadeList(ListView):
    model = Especialidade
    template_name = 'website/list/especialidade.html'


class EspecialidadeDetail(DetailView):
    model = Especialidade
    template_name = 'website/detail/especialidade.html'


# =====================================================
# PROFISSIONAL
# =====================================================

class ProfissionalCreate(CreateView):
    model = Profissional
    fields = ['usuario', 'crp', 'telefone', 'bio', 'especialidade']
    template_name = 'website/form.html'
    success_url = reverse_lazy('profissional-list')

    extra_context = {
        'titulo': 'Cadastro de Profissional',
        'botao': 'Cadastrar Profissional'
    }


class ProfissionalUpdate(UpdateView):
    model = Profissional
    fields = ['usuario', 'crp', 'telefone', 'bio', 'especialidade']
    template_name = 'website/form.html'
    success_url = reverse_lazy('profissional-list')

    extra_context = {
        'titulo': 'Editar Profissional',
        'botao': 'Salvar Alterações'
    }


class ProfissionalDelete(DeleteView):
    model = Profissional
    template_name = 'website/form.html'
    success_url = reverse_lazy('profissional-list')

    extra_context = {
        'titulo': 'Excluir Profissional',
        'botao': 'Confirmar Exclusão'
    }


class ProfissionalList(ListView):
    model = Profissional
    template_name = 'website/list/profissional.html'


class ProfissionalDetail(DetailView):
    model = Profissional
    template_name = 'website/detail/profissional.html'


# =====================================================
# AGENDA
# =====================================================

class AgendaCreate(CreateView):
    model = Agenda
    fields = ['profissional', 'dia_semana', 'hora_inicio', 'hora_fim', 'ativo']
    template_name = 'website/form.html'
    success_url = reverse_lazy('agenda-list')

    extra_context = {
        'titulo': 'Cadastro de Agenda',
        'botao': 'Cadastrar Agenda'
    }


class AgendaUpdate(UpdateView):
    model = Agenda
    fields = ['profissional', 'dia_semana', 'hora_inicio', 'hora_fim', 'ativo']
    template_name = 'website/form.html'
    success_url = reverse_lazy('agenda-list')

    extra_context = {
        'titulo': 'Editar Agenda',
        'botao': 'Salvar Alterações'
    }


class AgendaDelete(DeleteView):
    model = Agenda
    template_name = 'website/form.html'
    success_url = reverse_lazy('agenda-list')

    extra_context = {
        'titulo': 'Excluir Agenda',
        'botao': 'Confirmar Exclusão'
    }


class AgendaList(ListView):
    model = Agenda
    template_name = 'website/list/agenda.html'


class AgendaDetail(DetailView):
    model = Agenda
    template_name = 'website/detail/agenda.html'


# =====================================================
# CONSULTA
# =====================================================

class ConsultaCreate(CreateView):
    model = Consulta
    fields = ['paciente', 'profissional', 'data', 'hora', 'status', 'motivo']
    template_name = 'website/form.html'
    success_url = reverse_lazy('consulta-list')

    extra_context = {
        'titulo': 'Agendar Consulta',
        'botao': 'Agendar Consulta'
    }


class ConsultaUpdate(UpdateView):
    model = Consulta
    fields = ['paciente', 'profissional', 'data', 'hora', 'status', 'motivo']
    template_name = 'website/form.html'
    success_url = reverse_lazy('consulta-list')

    extra_context = {
        'titulo': 'Editar Consulta',
        'botao': 'Salvar Alterações'
    }


class ConsultaDelete(DeleteView):
    model = Consulta
    template_name = 'website/form.html'
    success_url = reverse_lazy('consulta-list')

    extra_context = {
        'titulo': 'Cancelar Consulta',
        'botao': 'Confirmar Cancelamento'
    }


class ConsultaList(ListView):
    model = Consulta
    template_name = 'website/list/consulta.html'


class ConsultaDetail(DetailView):
    model = Consulta
    template_name = 'website/detail/consulta.html'


# =====================================================
# PRONTUÁRIO
# =====================================================

class ProntuarioCreate(CreateView):
    model = Prontuario
    fields = [
        'consulta',
        'paciente',
        'profissional',
        'descricao',
        'diagnostico',
        'observacoes'
    ]

    template_name = 'website/form.html'
    success_url = reverse_lazy('prontuario-list')

    extra_context = {
        'titulo': 'Cadastro de Prontuário',
        'botao': 'Salvar Prontuário'
    }


class ProntuarioUpdate(UpdateView):
    model = Prontuario
    fields = [
        'consulta',
        'paciente',
        'profissional',
        'descricao',
        'diagnostico',
        'observacoes'
    ]

    template_name = 'website/form.html'
    success_url = reverse_lazy('prontuario-list')

    extra_context = {
        'titulo': 'Editar Prontuário',
        'botao': 'Salvar Alterações'
    }


class ProntuarioDelete(DeleteView):
    model = Prontuario
    template_name = 'website/form.html'
    success_url = reverse_lazy('prontuario-list')

    extra_context = {
        'titulo': 'Excluir Prontuário',
        'botao': 'Confirmar Exclusão'
    }


class ProntuarioList(ListView):
    model = Prontuario
    template_name = 'website/list/prontuario.html'


class ProntuarioDetail(DetailView):
    model = Prontuario
    template_name = 'website/detail/prontuario.html'


# =====================================================
# PAGAMENTO
# =====================================================

class PagamentoCreate(CreateView):
    model = Pagamento
    fields = ['consulta', 'valor', 'data_pagamento', 'status', 'metodo']
    template_name = 'website/form.html'
    success_url = reverse_lazy('pagamento-list')

    extra_context = {
        'titulo': 'Registrar Pagamento',
        'botao': 'Salvar Pagamento'
    }


class PagamentoUpdate(UpdateView):
    model = Pagamento
    fields = ['consulta', 'valor', 'data_pagamento', 'status', 'metodo']
    template_name = 'website/form.html'
    success_url = reverse_lazy('pagamento-list')

    extra_context = {
        'titulo': 'Editar Pagamento',
        'botao': 'Salvar Alterações'
    }


class PagamentoDelete(DeleteView):
    model = Pagamento
    template_name = 'website/form.html'
    success_url = reverse_lazy('pagamento-list')

    extra_context = {
        'titulo': 'Excluir Pagamento',
        'botao': 'Confirmar Exclusão'
    }


class PagamentoList(ListView):
    model = Pagamento
    template_name = 'website/list/pagamento.html'


class PagamentoDetail(DetailView):
    model = Pagamento
    template_name = 'website/detail/pagamento.html'