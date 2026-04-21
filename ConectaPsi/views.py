from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Agendamento


class AgendamentoCreate(CreateView):
    model = Agendamento
    fields = ['paciente', 'psicologo', 'horario', 'status']
    template_name = 'app/form.html'
    success_url = reverse_lazy('agendamento-list')
    extra_context = {
        'titulo': 'Novo Agendamento',
        'botao': 'Criar'
    }


class AgendamentoUpdate(UpdateView):
    model = Agendamento
    fields = ['paciente', 'psicologo', 'horario', 'status']
    template_name = 'app/form.html'
    success_url = reverse_lazy('agendamento-list')
    extra_context = {
        'titulo': 'Editar Agendamento',
        'botao': 'Atualizar'
    }


class AgendamentoDelete(DeleteView):
    model = Agendamento
    template_name = 'app/form.html'
    success_url = reverse_lazy('agendamento-list')
    extra_context = {
        'titulo': 'Excluir Agendamento',
        'botao': 'Confirmar exclusão'
    }


class AgendamentoList(ListView):
    model = Agendamento
    template_name = 'app/list/agendamento.html'


class AgendamentoDetail(DetailView):
    model = Agendamento
    template_name = 'app/detail/agendamento.html'