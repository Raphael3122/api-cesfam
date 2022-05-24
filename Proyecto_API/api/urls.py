from django.urls import path
from .views import MedicamentoView, RegisterView, UsuarioView, InsumoView

urlpatterns=[
    path('registro/',RegisterView.as_view(),name='register_list'),
    path('registro/<int:id>',RegisterView.as_view(),name='register_process'),
    
    # Este url es para la parte de medicamento
    path('medicamento/',MedicamentoView.as_view(),name='medicamento_list'),
    path('medicamento/<str:codigo>',MedicamentoView.as_view(),name='medicamento_process'),

    # ESTE URL ES PARA EL USUARIO
    
    path('usuario/',UsuarioView.as_view(),name='usuario_list'),
    path('usuario/<str:correo>&<password>',UsuarioView.as_view(),name='usuario_process'),
    
    # ESTE URL ES PARA Insumos medicos

    
    path('insumomedico/',InsumoView.as_view(),name='insumomedico_list'),
    
    path('insumomedico/<int:id>',InsumoView.as_view(),name='insumomedico_process'),
]