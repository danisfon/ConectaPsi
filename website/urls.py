from django.urls import path

from django.urls import path

from .views import (
    IndexView, 
    ContatoView, 
    SobreView,

    EspecialidadeCreate,
    EspecialidadeUpdate,
    EspecialidadeDelete,
    EspecialidadeList,
    EspecialidadeDetail,

    
    PacienteCreate,
    PacienteUpdate,
    PacienteDelete,
    PacienteList,
    PacienteDetail,

    ProfissionalCreate,
    ProfissionalUpdate,
    ProfissionalDelete,
    ProfissionalList,
    ProfissionalDetail,

    AgendaCreate,
    AgendaUpdate,
    AgendaDelete,
    AgendaList,
    AgendaDetail,


    ConsultaCreate,
    ConsultaUpdate,
    ConsultaDelete,
    ConsultaList,
    ConsultaDetail,

    ProntuarioCreate,
    ProntuarioUpdate,
    ProntuarioDelete,
    ProntuarioList,
    ProntuarioDetail,

    PagamentoCreate,
    PagamentoUpdate,
    PagamentoDelete,
    PagamentoList,
    PagamentoDetail,
)

urlpatterns = [


    path(
        'cadastrar/especialidade/',
        EspecialidadeCreate.as_view(),
        name='especialidade-create'
    ),

    path(
        'atualizar/especialidade/<int:pk>/',
        EspecialidadeUpdate.as_view(),
        name='especialidade-update'
    ),

    path(
        'excluir/especialidade/<int:pk>/',
        EspecialidadeDelete.as_view(),
        name='especialidade-delete'
    ),

    path(
        'listar/especialidade/',
        EspecialidadeList.as_view(),
        name='especialidade-list'
    ),

    path(
        'detalhar/especialidade/<int:pk>/',
        EspecialidadeDetail.as_view(),
        name='especialidade-detail'
    ),



    path(
        'cadastrar/paciente/',
        PacienteCreate.as_view(),
        name='paciente-create'
    ),

    path(
        'atualizar/paciente/<int:pk>/',
        PacienteUpdate.as_view(),
        name='paciente-update'
    ),

    path(
        'excluir/paciente/<int:pk>/',
        PacienteDelete.as_view(),
        name='paciente-delete'
    ),

    path(
        'listar/paciente/',
        PacienteList.as_view(),
        name='paciente-list'
    ),

    path(
        'detalhar/paciente/<int:pk>/',
        PacienteDetail.as_view(),
        name='paciente-detail'
    ),


    path(
        'cadastrar/profissional/',
        ProfissionalCreate.as_view(),
        name='profissional-create'
    ),

    path(
        'atualizar/profissional/<int:pk>/',
        ProfissionalUpdate.as_view(),
        name='profissional-update'
    ),

    path(
        'excluir/profissional/<int:pk>/',
        ProfissionalDelete.as_view(),
        name='profissional-delete'
    ),

    path(
        'listar/profissional/',
        ProfissionalList.as_view(),
        name='profissional-list'
    ),

    path(
        'detalhar/profissional/<int:pk>/',
        ProfissionalDetail.as_view(),
        name='profissional-detail'
    ),


    path(
        'cadastrar/agenda/',
        AgendaCreate.as_view(),
        name='agenda-create'
    ),

    path(
        'atualizar/agenda/<int:pk>/',
        AgendaUpdate.as_view(),
        name='agenda-update'
    ),

    path(
        'excluir/agenda/<int:pk>/',
        AgendaDelete.as_view(),
        name='agenda-delete'
    ),

    path(
        'listar/agenda/',
        AgendaList.as_view(),
        name='agenda-list'
    ),

    path(
        'detalhar/agenda/<int:pk>/',
        AgendaDetail.as_view(),
        name='agenda-detail'
    ),


    path(
        'cadastrar/consulta/',
        ConsultaCreate.as_view(),
        name='consulta-create'
    ),

    path(
        'atualizar/consulta/<int:pk>/',
        ConsultaUpdate.as_view(),
        name='consulta-update'
    ),

    path(
        'excluir/consulta/<int:pk>/',
        ConsultaDelete.as_view(),
        name='consulta-delete'
    ),

    path(
        'listar/consulta/',
        ConsultaList.as_view(),
        name='consulta-list'
    ),

    path(
        'detalhar/consulta/<int:pk>/',
        ConsultaDetail.as_view(),
        name='consulta-detail'
    ),


    path(
        'cadastrar/prontuario/',
        ProntuarioCreate.as_view(),
        name='prontuario-create'
    ),

    path(
        'atualizar/prontuario/<int:pk>/',
        ProntuarioUpdate.as_view(),
        name='prontuario-update'
    ),

    path(
        'excluir/prontuario/<int:pk>/',
        ProntuarioDelete.as_view(),
        name='prontuario-delete'
    ),

    path(
        'listar/prontuario/',
        ProntuarioList.as_view(),
        name='prontuario-list'
    ),

    path(
        'detalhar/prontuario/<int:pk>/',
        ProntuarioDetail.as_view(),
        name='prontuario-detail'
    ),

    path(
        'cadastrar/pagamento/',
        PagamentoCreate.as_view(),
        name='pagamento-create'
    ),

    path(
        'atualizar/pagamento/<int:pk>/',
        PagamentoUpdate.as_view(),
        name='pagamento-update'
    ),

    path(
        'excluir/pagamento/<int:pk>/',
        PagamentoDelete.as_view(),
        name='pagamento-delete'
    ),

    path(
        'listar/pagamento/',
        PagamentoList.as_view(),
        name='pagamento-list'
    ),

    path(
        'detalhar/pagamento/<int:pk>/',
        PagamentoDetail.as_view(),
        name='pagamento-detail'
    ),

]
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("contato/", ContatoView.as_view(), name="contato"),
    path("sobre/", SobreView.as_view(), name="sobre")
]
