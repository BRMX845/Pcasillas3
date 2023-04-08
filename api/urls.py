from django.urls import path
from .views import UsuariosList ,CasillaList,DepartamentoList,AlquilerCasillasList
urlpatterns = [
    path('Usuarios/',UsuariosList.as_view(),name='usuario_list' ),
    path('departamentos/',DepartamentoList.as_view()),
    path('casillas/',CasillaList.as_view()),
    path('alquilercasillas/',AlquilerCasillasList.as_view())
]